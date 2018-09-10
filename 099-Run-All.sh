#!/bin/bash
set -x
cd $( dirname "${BASH_SOURCE[0]}" )
ROOT=${PWD}

# exec the rest of this this script's stdout and stdrrr to the log
exec &> >(stdbuf -i 0 -o 0 -e 0 tee "${PWD}/090-logs/$(date +%Y-%m-%d-%H-%M-%S.log)")

date

LOCKFILE="${ROOT}/010-init/.flockfile.099-Run-All.sh"

function cleanup {
  cd "${ROOT}"
  rm -f ${LOCKFILE}
  if [[ -e ./010-init/.shutdown.099-Run-All.sh ]]
  then
    sleep 1m
    [[ -e ./010-init/.shutdown.099-Run-All.sh ]] && /sbin/shutdown -h now &
  fi

  exit
}

trap cleanup INT TERM EXIT

function run {
  cd "${ROOT}"
  eval stdbuf -o 0 -e 0 time ${*}
}

# wait for file lock
(flock --verbose -x -w 10 222 || exit 1
  run git pull origin master
  run ./027-Generate_Master_Model_Python.sh
  run ./046-Update_050_Automated_Input_Data.sh
  run ./055-Generate_Model_Outputs.sh
  run ./070-Data_Portal_Push_Outputs/075-Upload_Automated_Model_Outputs.sh
  run git add 030-Master_Model_Python 050-Automated_Input_Data 060-Automated_Model_Outputs
  run git commit -m "HCEM updates on $(date '+%Y-%m-%d %H:%M') from rev $(git rev-parse --short HEAD)"
  run git push
) 222> ${LOCKFILE}
date


