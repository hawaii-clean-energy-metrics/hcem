#!/usr/bin/env python2
import xlrd
import urllib2
import StringIO
import re
import datetime
import csv
import os
from collections import namedtuple, Counter, defaultdict
import sys


def col_letter(idx):
    letters = ""
    while idx:
        idx, rem = divmod(idx-1,26)
        letters = chr(rem+65) + letters
    return letters

def safe_str(val, quote=None):
    if val is None:
        val = ""

    if isinstance(val, datetime.datetime):
        isostr = val.isoformat()
        if (val.hour, val.minute, val.second) == (0, 0, 0):
            isostr = isostr.split("T", 1)[0]
        val = isostr

    isfloat = isinstance(val, float)
    val = val.encode('utf-8') if isinstance(val, unicode) else str(val)
    if isfloat and val.endswith('.0'):
        val = val[:-2]

    if quote is not None:
        val = "{}{}{}".format(quote, val, quote)
    return val


def sheet_to_values(xl_sheet):

    datemode = xl_sheet.book.datemode

    def get_cell_value(cell):
        val = cell.value
        if cell.ctype == xlrd.XL_CELL_EMPTY:
            val = None
        elif cell.ctype == xlrd.XL_CELL_DATE:
            try:
                timetuple = xlrd.xldate_as_tuple(cell.value, datemode)
                val = datetime.datetime(*timetuple)
            except:
                val = cell.value
        return val

    rows = [None] * xl_sheet.nrows
    for row_idx in range(xl_sheet.nrows):
        row = [None] * xl_sheet.ncols
        for col_idx in range(xl_sheet.ncols):
            cell = xl_sheet.cell(row_idx, col_idx)
            row[col_idx] = get_cell_value(cell)

        rows[row_idx] = row
    return rows


def row_to_strs(row, quote='"'):
    return [safe_str(cell, quote) for cell in row]


def values_to_strs2d(rows, quote='"'):
    return [row_to_strs(row) for row in rows]


def strs2d_to_csv(rows):
    return "\n".join([",".join(row) for row in rows])


def rows_to_csv(rows, quote='"'):
    return strs2d_to_csv(values_to_strs2d(rows, quote))


def sheet_to_csv(xl_sheet):
    return strs2d_to_csv(values_to_strs2d(sheet_to_values(xl_sheet)))


def load_remote_xl_workbook(url):
    response = urllib2.urlopen(url)
    stringio = StringIO.StringIO(response.read())
    filedata = stringio.getvalue()
    stringio.close()
    return xlrd.open_workbook(file_contents=filedata)


def iterate_through_sheets(sheets):
    for sheet in sheets:
        if sheet not in sheet_names:
            print "{} not found in {}".format(sheet, sheet_names)
            continue
        xl_sheet = workbook.sheet_by_name(sheet)
        csv = sheet_to_csv(xl_sheet)
        print csv


def fetch_remote_worksheet_as_rows(url, sheet_name):
    rows = []
    workbook = load_remote_xl_workbook(url)
    if workbook and sheet_name in workbook.sheet_names():
        xl_sheet = workbook.sheet_by_name(sheet_name)
        rows = sheet_to_values(xl_sheet)

    return rows


class Loader(object):

    EXT_EXCEL = ["xls", "xlsx"]
    EXT_CSV = ["csv"]

    def __init__(self, url, sheetname=None):

        urlparts = list(urllib2.urlparse.urlsplit(url))
        if not urlparts[0]:
            urlparts[0] = "file"
            urlparts[2] = os.path.abspath(urlparts[2])

        url = urllib2.urlparse.urlunsplit(urlparts)

        self.url = url
        self.sheetname = sheetname
        self.extension = urlparts[2].lower().rsplit(".", 1)[-1]

    def get_filedata(self):
        response = urllib2.urlopen(self.url)
        stringio = StringIO.StringIO(response.read())
        filedata = stringio.getvalue()
        stringio.close()
        return filedata

    def get_rows(self):
        filedata = self.get_filedata()
        if self.extension in self.EXT_EXCEL:
            return self.get_rows_from_excel(filedata)

        if self.extension in self.EXT_CSV:
            return self.get_rows_from_csv(filedata)

        return []

    def get_csv(self):
        rows = self.get_rows()
        return rows_to_csv(rows)

    def get_rows_from_excel(self, filedata):
        xl_sheet = None

        xl_workbook = xlrd.open_workbook(file_contents=filedata)
        if xl_workbook:
            sheetnames = xl_workbook.sheet_names()
            sheetname = self.sheetname if self.sheetname else 0

            if sheetname in sheetnames:
                xl_sheet = xl_workbook.sheet_by_name(sheetname)
            else:
                snum = None
                try:
                    snum = int(sheetname)
                except:
                    pass
                if snum is not None and snum < len(sheetnames):
                    xl_sheet = xl_workbook.sheet_by_index(snum)

        values = []
        if xl_sheet is not None:
            values = sheet_to_values(xl_sheet)

        return values

    def get_rows_from_csv(self, filedata):
        rows = []
        csvfile = StringIO.StringIO(filedata)
        csvreader = csv.reader(csvfile, delimiter=",", quotechar="\"")
        for csvrow in csvreader:
            row = csvrow[:]
            rows.append(row)
        return rows



class Spreadsheet(object):
    # headerrows:
    #   None will eat header rows
    #   0 will disable
    def __init__(self, url, sheetname=None, headerrow=None, safe_header=False):
        loader = Loader(url, sheetname)
        rows = loader.get_rows()

        self.fields = []
        self.rows = []
        self.valid_header = False

        if headerrow is not None:
            while headerrow and len(rows):
                rows.pop(0)
                headerrow -= 1
        else:
            while len(rows) and ("" in rows[0] or None in rows[0]):
                rows.pop(0)

        if not len(rows):
            return

        self.fields = [col for col in rows[0]]

        if not safe_header and any(self.fields):
            self.valid_header = True
            rows = rows[1:]

        col_fieldnames = ["{}".format(col_letter(i+1)) for i,col in enumerate(self.fields)]
        # fixup invalid header entries w/ Col
        if safe_header:
            tuple_fieldnames = col_fieldnames
        else:
            tuple_fieldnames = [col_fieldnames[i] if not col else "{}".format(col) for i,col in enumerate(self.fields)]
            tuple_fieldnames = ["_".join([subfield for subfield in re.split("\W", field) if subfield]) for field in tuple_fieldnames]
            tuple_fieldnames = [str(i) if not col else "{}".format(col) for i,col in enumerate(tuple_fieldnames)]
            tuple_fieldnames = ["f"+f if f and f[0].isdigit() else f for f in tuple_fieldnames]

        self.header = namedtuple("header", tuple_fieldnames)
        self.rows = []
        for row in rows:
            if len(row) != len(self.fields):
                sys.stderr.write("row={} not correct length ({})\n".format(row, len(self.fields)))
            else:
                self.rows.append(self.header._make(row))

    @property
    def nrows(self):
        return len(self.rows)


    @property
    def ncols(self):
        return len(self.fields)


    def get_csv(self):
        allrows = self.rows
        if self.valid_header:
            allrows = [self.fields] + allrows

        return rows_to_csv(allrows)


def parse_args(args):

    url = str(args[0]) if args and len(args) > 0 else None
    sheet = str(args[1]) if args and len(args) > 1 else None

    header = None
    if args and len(args) > 2:
        try:
            header = int(args[2])
        except:
            header = None

    return url, sheet, header


def main(args):
    url, sheet, header = parse_args(args[1:])

    if not url:
        print "Usage:\n  {} URL [SHEETNAME] [# of header row]".format(args[0])
        return -1

    print Spreadsheet(url, sheet, header).get_csv()

    return 0

if __name__ == "__main__":
    from sys import argv, exit
    exit(main(argv))
