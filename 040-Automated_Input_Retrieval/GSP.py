#!/usr/bin/env python2
import Spreadsheet
import sys

def main(args):
    url = args.pop(0)
    print "url={}".format(url)
    sheet = Spreadsheet.Spreadsheet(url, 0, 0)
    sheet.rows = [row for row in sheet.rows if row.Description == "All industry total"]
    print sheet.get_csv()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
