#!/usr/bin/env python2
import Spreadsheet
from collections import namedtuple, Counter, defaultdict
import sys

URL_COMPLETE_SEDS = "Complete_SEDS.csv"
URL_COMPLETE_SEDS = "https://www.eia.gov/state/seds/sep_update/Complete_SEDS_update.csv"
URL_SEDS_DESC_SHEET = ["Codes_and_Descriptions.xlsx", "MSN Descriptions"]
URL_SEDS_DESC_SHEET[0] = "https://www.eia.gov/state/seds/CDF/Codes_and_Descriptions.xlsx"


def get_msn_codes_and_descriptions_data():
    ss = Spreadsheet.Loader(*URL_SEDS_DESC_SHEET)
    return ss.get_rows()


def get_msn_description_table():
    rows = get_msn_codes_and_descriptions_data()

    header = ("MSN", "Description", "Unit")
    MSNDescription = namedtuple("MSNDescription", header)
    header = map(str.decode, header)
    ridx = 0
    msn_description_table = {}
    searching_for_header = True
    while ridx < len(rows):
        row = rows[ridx]
        ridx += 1
        if searching_for_header:
            searching_for_header = row[1:] != header
        else:
            desc = MSNDescription(*row[1:])
            msn_description_table[desc[0]] = desc

    return msn_description_table


def get_seds_for_state(state):
    rows = Spreadsheet.Loader(URL_COMPLETE_SEDS).get_rows()
    SEDS = namedtuple("SEDS", rows[0])
    entries = []
    for row in rows[1:]:
        entry = SEDS(*row)
        if entry.StateCode == state:
            entries.append(entry)
    return entries


def get_unique_counts_for_tuples(tuples):
    assert len(tuples)
    assert isinstance(tuples, list)
    ttype = type(tuples[0])
    fields = ttype._fields
    n = len(fields)
    counts = [None] * n

    for i in xrange(n):
        counts[i] = Counter([tup[i] for tup in tuples])

    return ttype._make(counts)


def make_state_table(state):
    seds = get_seds_for_state(state)
    #counts = get_unique_counts_for_tuples(seds)
    year_counts = Counter()
    alldata = defaultdict(dict)
    for entry in seds:
        msn, year, data = entry.MSN, entry.Year, entry.Data
        row = alldata[msn]
        assert year not in row
        year_counts[year] += 1
        row[year] = data

    msn_description_table = get_msn_description_table()

    #years = ["{:>4}".format(year) for year in sorted(counts.keys())]
    years = ["{:>4}".format(year) for year in sorted(year_counts.keys())]
    header = ["State", "Description", "MSN", "Unit"] + years

    rows = [header]
    empty_desc = namedtuple("foo", "Description Unit")("","")
    for msn,row in sorted(alldata.iteritems()):
        desc = msn_description_table.get(msn, empty_desc)
        row = [state, desc.Description, msn, desc.Unit] + [row.get(year, None) for year in years]
        rows.append(row)

    return rows


def make_hawaii_seds_csv_text():
    hi_rows = make_state_table("HI")
    csv_text = Spreadsheet.rows_to_csv(hi_rows)
    return csv_text


def main(args):
    global URL_COMPLETE_SEDS, URL_SEDS_DESC_SHEET
    if len(args) > 0:
        URL_COMPLETE_SEDS = args[0]

    if len(args) > 1:
        URL_SEDS_DESC_SHEET[0] = args[1]

    print make_hawaii_seds_csv_text()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
