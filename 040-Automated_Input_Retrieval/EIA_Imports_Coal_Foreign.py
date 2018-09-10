#!/usr/bin/env python2
import Spreadsheet
import sys

EIA_URL="http://www.eia.gov/coal/archive/coal_historical_imports.xlsx"

def main(args):
    url = EIA_URL if not args else args[0]
    sheet = Spreadsheet.Spreadsheet(url, 0, 3)

    sheet.rows = [row for row in sheet.rows if row.Customs_District == "Honolulu, HI"]

    print sheet.get_csv()

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
