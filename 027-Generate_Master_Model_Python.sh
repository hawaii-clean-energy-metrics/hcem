#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="${BASEDIR}/010-init"
source ${HCEMINITDIR}/sourceme

time \
  "${BASEDIR}/025-Excel_to_Python/xl2py" \
  --input-xlsx "${BASEDIR}/020-Master_Model_Spreadsheet/Master-Hawaii_Clean_Energy_Metrics.xlsx" \
  --output-py "${BASEDIR}/030-Master_Model_Python/"

