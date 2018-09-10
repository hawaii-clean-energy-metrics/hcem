#!/usr/bin/env python2
import Spreadsheet
import sys

URL="https://www.eia.gov/dnav/pet/hist_xls/RWTCm.xls"

def main(*args):
    if not args:
        args = [URL]

    for url in args:
        print Spreadsheet.Spreadsheet(url, 1, 1).get_csv()

    return 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
