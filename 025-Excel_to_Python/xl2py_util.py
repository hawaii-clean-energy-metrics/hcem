#!/usr/bin/env python
import sys
import xl2py_tokenizer as tokenizer
import time
import datetime
import os
import shutil
from collections import Counter, OrderedDict, defaultdict
import re

from calendar import timegm as struct_time_to_timestamp

SECONDS_PER_DAY = 24 * 60 * 60 # 86400
EXCEL_EPOCH_OFFSET_FROM_UNIX_EPOCH_IN_DAYS = -25569


ROWCOL = re.compile(r'^(?P<col>[A-Z]+)?(?P<row>[0-9]+)?$')

def datetime_to_excel_time(dt):
    if not isinstance(dt, datetime.datetime):
        return None

    struct_time = time.struct_time((dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, 0, 0, 0))
    timestamp = struct_time_to_timestamp(struct_time)
    timestamp = timestamp / SECONDS_PER_DAY
    timestamp = timestamp - EXCEL_EPOCH_OFFSET_FROM_UNIX_EPOCH_IN_DAYS
    return timestamp


def col_letter_val(inletters):
    idx = 0
    letters = inletters.upper()
    while len(letters):
        letter, letters = letters[0],letters[1:]
        idx = idx * 26 + ord(letter) - 64
    return idx


def name_to_colrow(name):
    colrow = ROWCOL.match(name).groups()
    col = col_letter_val(colrow[0]) if colrow[0] else 0
    row = int(colrow[1]) if colrow[1] else 0
    return col, row


def setup_logger(name=None):
    import logging
    if name is None:
        name = __name__
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)
    assert os.path.exists(path)


def col_letter(idx):
    letters = ""
    while idx:
        idx, rem = divmod(idx-1,26)
        letters = chr(rem+65) + letters
    return letters




def cell_name(worksheet, boundaries):
    cellname = lambda colrow: "{}{}".format(col_letter(colrow[0]), colrow[1])
    result = "{}".format(cellname(boundaries[:2]))
    if worksheet:
        result = "'{}':{}".format(worksheet, result)
    if len(boundaries) > 2:
        result += ":{}".format(cellname(boundaries[2:]))
    return result


def col_letter(idx):
    letters = ""
    while idx:
        idx, rem = divmod(idx - 1, 26)
        letters = chr(rem + 65) + letters
    return letters


def safe_str(val):
    return val.encode('utf-8') if isinstance(val, unicode) else str(val)


def python_rep(val):
    func = ""
    quotes = ''
    if isinstance(val, basestring):
        quotes = "'''" if '"' in val or '\n' in val else '"'
        val = val.encode('utf-8')
    elif isinstance(val, datetime.datetime):
        val = str(datetime_to_excel_time(val))
    else:
        isfloat = isinstance(val, float)
        val = str(val)
        if isfloat and val.endswith(".0"):
            val = val[:-2]

    rep = "{}{}{}{}".format(func, quotes, val, quotes)

    return rep


def compute_range_tuple(in_range_string, context_worksheet_name):
    range_string = in_range_string
    if not '!' in range_string:
        range_string = "'{}'!{}".format(context_worksheet_name, range_string)

    tokens = range_string
    tokens = tokens.split("!")
    assert len(tokens) == 2
    worksheet_title = xlat_worksheet(tokens[0].strip("' "))
    tokens = tokens[1].replace("$", "")
    tokens = tokens.split(":")
    if len(tokens) == 1:
        tokens.append(tokens[0])

    if len(tokens) != 2:
        sys.stderr.write("#Unable to parse range, in_range_str={}, range_str={}\n".format(in_range_string, range_string))
        colmin = colmax = rowmin = rowmax = 0
    else:
        colmin,rowmin = name_to_colrow(tokens[0])
        colmax,rowmax = name_to_colrow(tokens[1])

    return (worksheet_title, (colmin, rowmin, colmax, rowmax))



WORKSHEET_XLAT = {
    " ": "_",
    "(": "_",
    ")": "_",
    ",": "_"
}

WORKSHEET_XLAT_RE = re.compile("|".join(map(re.escape, WORKSHEET_XLAT.keys())))


def xlat_worksheet(name):
    return WORKSHEET_XLAT_RE.sub(lambda x: WORKSHEET_XLAT[x.group(0)], name)




class Emitter(object):
    python_indent = " " * 4
    python_prefix = "    "
    python_eol = "\n"

    def __init__(self):
        self.lines = []
        self.indent = 0

    @property
    def emit(self):
        result = "\n".join(self.lines)
        self.lines = []
        return result

    @emit.setter
    def emit(self, value):
        vstr = self.python_indent * min(self.indent,10) + value
        # sys.stderr.write(".")
        self.lines.append(vstr)

    def write_file(self, filename):
        with open(filename,"wt") as out:
            out.write(self.emit)
            return True
        return False
