#!/bin/bash
FILES=$(ls -1 Dashboard* | cut -d. -f 1 | sort | uniq | sort -V)

IFS=$'\n'
for file in ${FILES}
do
    METRIC=$(echo $file | cut -d\  -f 2 | cut -c2-)
    DASHBOARD="$file"
    FILENAME_CSV="${file}.csv"
    FILENAME_XLSX="${file}.xlsx"
    echo METRIC=\"$METRIC\" DASHBOARD=\"$DASHBOARD\" FILENAME_CSV=\"$FILENAME_CSV\" FILENAME_XLSX=\"$FILENAME_XLSX\" ./upload.py metadata/resources/hepf-dashboard.ini
done
