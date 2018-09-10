#!/usr/bin/env python2
import Spreadsheet
import links_in_url
import sys

BASE_URL = "https://www.epa.gov/statelocalenergy/state-co2-emissions-fossil-fuel-combustion"


def get_co2_url():
    links = links_in_url.get_links_matching(BASE_URL, ["xlsx"])
    assert len(links) == 1, "Cannot find single xlsx link to CO2 Emissions on {}".format(BASE_URL)
    return links[0]


def filter_co2_by_states(data, states):
    state_found = False
    rows = []
    for row in data.rows:
        if row.State:
            state_found = row.State in states
        if state_found:
            rows.append(row)
    data.rows = rows
    return data


def get_hawaii_co2_emissions_csv_text():
    co2 = get_co2_url()
    data = Spreadsheet.Spreadsheet(co2, None, 2)
    data = filter_co2_by_states(data, ["Hawaii"])
    text = data.get_csv()
    return text


def main():
    print get_hawaii_co2_emissions_csv_text()
    return 0

if __name__ == "__main__":
    sys.exit(main())
