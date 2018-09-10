#!/usr/bin/env python2
import Spreadsheet
import re
import sys

def isclose(a, b, rel_tol=1e-08, abs_tol=0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def fixup_population(rows):

    def cast_values(value):
        if type(value) not in [type(0.0), type(0)]:
            value = Spreadsheet.safe_str(value).strip()

            try:
                fval = float(value)
                value = fval
            except:
                pass

        if type(value) == type(0.0):
            if isclose(value, int(value)):
                value = int(value)

        return value

    rows = [[str(cast_values(v)) for v in row] for row in rows]

    # Skip rows until first header row
    while rows and not any(['Resident population' in v for v in rows[0] if v]):
        rows.pop(0)

    # Combine first two header rows into one
    rows[1] = ["{}{}".format(v1, v2) for v1,v2 in zip(rows[0], rows[1])]
    rows.pop(0)

    # Remove entirely empty rows and rows of wrong length
    rows = [row for row in rows if len(row) > 1 and "".join(row)]

    # Combine first two columns w/ weird date-formatting into a canonical date format
    oldrows = rows[:]
    for i,row in enumerate(rows):
        car, cdr = row[0], row[1:]
        if cdr[0].lower().startswith("july 1"):
            car = oldrows[i-1][0] if not car and i else car
            car = "{}-07-01".format(car)
        if cdr[0].lower().startswith("april 1"):
            car = oldrows[i-1][0] if not car and i else car
            car = "{}-04-01".format(car)

        rows[i] = [car] + cdr[1:]

    return rows


def fetch_DBEDT_databook_population_rows():
    url = "http://files.hawaii.gov/dbedt/economic/databook/Data_Book_time_series/sec01update.xls"
    population_sheet_name = "01.04"
    ss = Spreadsheet.Loader(url, population_sheet_name)
    return ss.get_rows()


def get_fixed_population_csv():
    pop_rows = fetch_DBEDT_databook_population_rows()
    fixed_pop_rows = fixup_population(pop_rows)
    csv_text = Spreadsheet.rows_to_csv(fixed_pop_rows)
    return csv_text


if __name__ == "__main__":
    print get_fixed_population_csv()
