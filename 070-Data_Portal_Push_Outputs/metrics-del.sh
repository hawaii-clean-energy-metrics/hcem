#!/bin/bash
set -x
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

PATTERN="${1:-Dashboard\ M*.csv}"

IFS=$'\n'
for f in $(ls -1 *${PATTERN}* | sort -rV | cut -d\. -f 1 | uniq)
do
    DASHBOARD="${f}"
    FILENAME_CSV="${DASHBOARD}.csv"
    FILENAME_XLSX="${DASHBOARD}.xlsx"
    METRIC=$(echo "${DASHBOARD}" | cut -d\  -f2 | cut -c2-)
    ID="hawaii-clean-energy-metric-${METRIC}" ${BASEDIR}/upload.py ${BASEDIR}/package_delete.ini
done

