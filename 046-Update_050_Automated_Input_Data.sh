#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="${BASEDIR}/010-init"
source ${HCEMINITDIR}/sourceme

"${BASEDIR}/040-Automated_Input_Retrieval/045-Update_050_Automated_Input_Data.sh"
