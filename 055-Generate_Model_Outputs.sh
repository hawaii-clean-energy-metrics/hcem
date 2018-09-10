#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="${BASEDIR}/010-init"
source ${HCEMINITDIR}/sourceme

DATESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
DESTBASEDIR="${BASEDIR}/060-Automated_Model_Outputs"
INPUTSDIR="${BASEDIR}/050-Automated_Input_Data"
XL2PY="${BASEDIR}/030-Master_Model_Python/xl2py"

function md5of() {
    if [ -e "${1}" ]
    then
        sha256sum ${1} | cut -c-64
    else
        echo "${FILE} not found"
    fi
}


function compare_and_delete_if_same(){
    echo "Comparing ${1} to ${2}..."
    OLD_MD5=$(md5of "${1}")
    NEW_MD5=$(md5of "${2}")
    echo "${OLD_MD5} ${1}"
    echo "${NEW_MD5} ${2}"

    if [ "${OLD_MD5}" == "${NEW_MD5}" ]
    then
       shift
       echo "same...deleting ${*}"
       rm ${*}
    else
        echo "different...keeping ${2}"
    fi
}


function init_dir() {
    DESTDIR="${DESTBASEDIR}/${1}"
    DEST="${DESTDIR}/${1}_${DATESTAMP}.csv"
    mkdir -p "${DESTDIR}"
    OLD_FILE=$(ls -1 ${DESTDIR}/${1}_????-??-??-??-??-??.csv | tail -1)
    XLSX="${DESTDIR}/${1}_${DATESTAMP}.xlsx"
    echo "DESTDIR=${DESTDIR}"
    echo "DEST=${DEST}"
    echo "OLD_FILE=${OLD_FILE}"
}


function run_model_for_worksheet() {
    init_dir ${1}

    echo "Generating .csv and .xlsx of '${1}'"
    echo "${DEST}"
    echo "${XLSX}"

    time "${XL2PY}" \
      --output-xlsx="${XLSX}" \
      --output-csv="${DEST}" \
      --input-updates-dir="${INPUTSDIR}" \
      ${1}  \

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}" "${XLSX}"
}


function run_charts() {
    run_model_for_worksheet Charts_Data_M1
    run_model_for_worksheet Charts_Data_M1_Extra
    run_model_for_worksheet Charts_Data_M2
    run_model_for_worksheet Charts_Data_M3
    run_model_for_worksheet Charts_Data_M4_Cost
    run_model_for_worksheet Charts_Data_M4_Price
    run_model_for_worksheet Charts_Data_M5_Monthly
    run_model_for_worksheet Charts_Data_M6
    run_model_for_worksheet Charts_Data_M10
    run_model_for_worksheet Charts_Data_M11
    run_model_for_worksheet Charts_Data_M12_Local_Fuel
    run_model_for_worksheet Charts_Data_M12_Transportation
    run_model_for_worksheet Charts_Data_M13
    run_model_for_worksheet Charts_Data_M14
    run_model_for_worksheet Charts_Data_M15
    run_model_for_worksheet Charts_Data_M16
}

function run_dashboard() {
    run_model_for_worksheet Dashboard_M1
    run_model_for_worksheet Dashboard_M2_Annual
    run_model_for_worksheet Dashboard_M2_Imports_Data
    run_model_for_worksheet Dashboard_M2_Monthly
    run_model_for_worksheet Dashboard_M3
    run_model_for_worksheet Dashboard_M4_Cost_Annual
    run_model_for_worksheet Dashboard_M4_Cost_Monthly
    run_model_for_worksheet Dashboard_M4_Price_Annual
    run_model_for_worksheet Dashboard_M4_Price_Monthly
    run_model_for_worksheet Dashboard_M5_Cost_Monthly
    run_model_for_worksheet Dashboard_M5_Price_Annual
    run_model_for_worksheet Dashboard_M5_Price_Monthly
    run_model_for_worksheet Dashboard_M6_Quarterly
    run_model_for_worksheet Dashboard_M8
    run_model_for_worksheet Dashboard_M8_Alt
    run_model_for_worksheet Dashboard_M10_RPS
    run_model_for_worksheet Dashboard_M11_EEPS
    run_model_for_worksheet Dashboard_M11_HCEI
    run_model_for_worksheet Dashboard_M12_Local_Fuel
    run_model_for_worksheet Dashboard_M12_Transportation
    run_model_for_worksheet Dashboard_M13
    run_model_for_worksheet Dashboard_M14
    run_model_for_worksheet Dashboard_M15
    run_model_for_worksheet Dashboard_M16_EEPS
}


run_dashboard

