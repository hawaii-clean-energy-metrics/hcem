#!/usr/bin/env python2
import Spreadsheet
import sys

URL="https://www.eia.gov/dnav/pet/hist_xls/RBRTEm.xls"

DELIM=","

def main(url):
    if not url:
        return -1
    sheet = Spreadsheet.Spreadsheet(url, 1, 2)
    text = sheet.get_csv()
    print text
    return 0

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = [URL]
    sys.exit(main(args[0]))
