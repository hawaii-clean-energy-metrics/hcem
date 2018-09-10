#!/usr/bin/env python2
import Spreadsheet
import re
from collections import namedtuple, Counter, defaultdict
import sys


DELIM=","


def find(pattern, basedir = None):
    import fnmatch
    import os
    files = []
    if basedir is None:
        basedir = "."
    for dirpath, dirnames, filenames in os.walk(basedir):
        for filename in fnmatch.filter(filenames, pattern):
            files.append(os.path.join(dirpath, filename))
    return files



def main(args):
    if not args:
        return -1

    files = list(sorted(args))

    header = Spreadsheet.Spreadsheet(files[-1],0).header
    fields = header._fields

    print DELIM.join(Spreadsheet.row_to_strs(fields))

    for fname in files:
        sys.stderr.write("Extracting Petroleum Import entries for Hawaii from {}...\n".format(fname))
        blank = header(*[str()] * len(fields))
        sheet = Spreadsheet.Spreadsheet(fname, 0)
        for row in sheet.rows:
            tmp = blank._replace(**row._asdict())
            if tmp.PORT_STATE in ["HAWAII", "HI"]:
                print DELIM.join(Spreadsheet.row_to_strs(tmp))

    return 0

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = find("*.xls", ".")
    sys.exit(main(args))
