#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="${BASEDIR}/010-init"
source ${HCEMINITDIR}/sourceme

DATESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
DESTBASEDIR="${BASEDIR}/060-Automated_Model_Outputs"
INPUTSDIR="${BASEDIR}/050-Automated_Input_Data"
XL2PY="${BASEDIR}/030-Master_Model_Python/xl2py"


function compare_and_delete_if_same(){
    echo "Comparing ${1} to ${2}..."
    A=${1}
    B=${2}
    if [ ${1: -5} == ".xlsx" ]
    then
        TDIR=$(mktemp -d)
        A="${TDIR}/a"
        B="${TDIR}/b"
        echo "Extracting .xlsx files to ${A} and ${B}"
        unzip -q "${1}" -d "${A}" -x docProps/core.xml
        unzip -q "${2}" -d "${B}" -x docProps/core.xml
    fi

    if diff -rbq "${A}" "${B}"
    then
        echo "same...deleting ${2}"
        rm -v "${2}"
    else
        echo "${2} is different, keeping"
    fi

    # cleanup mktemp dir created when extracting xlsx files
    if [ -d "${TDIR}" ]
    then
      rm -rf ${TDIR}
    fi
}


function run_model_for_worksheet() {
    echo "Generating .csv and .xlsx of '${1}'"
    DESTDIR="${DESTBASEDIR}/${1}"
    mkdir -p "${DESTDIR}"
    MOST_RECENT_CSV=$(ls -1 ${DESTDIR}/${1}_????-??-??-??-??-??.csv | tail -1)
    MOST_RECENT_XLSX=$(ls -1 ${DESTDIR}/${1}_????-??-??-??-??-??.xlsx | tail -1)
    NEW_CSV="${DESTDIR}/${1}_${DATESTAMP}.csv"
    NEW_XLSX="${DESTDIR}/${1}_${DATESTAMP}.xlsx"
    echo "DESTDIR=${DESTDIR}"
    echo "NEW_CSV=${NEW_CSV}"
    echo "NEW_XSLX=${NEW_XLSX}"

    time "${XL2PY}" \
      --output-csv="${NEW_CSV}" \
      --output-xlsx="${NEW_XLSX}" \
      --input-updates-dir="${INPUTSDIR}" \
      ${1} 

    compare_and_delete_if_same "${MOST_RECENT_CSV}" "${NEW_CSV}" 
    compare_and_delete_if_same "${MOST_RECENT_XLSX}" "${NEW_XLSX}"
}


function run_worksheets() {
    for worksheet in ${*}
    do
        run_model_for_worksheet $worksheet
    done 
}


function run_charts() {
    run_worksheets \
        Charts_Data_M1 \
        Charts_Data_M1_Extra \
        Charts_Data_M2 \
        Charts_Data_M3 \
        Charts_Data_M4_Cost \
        Charts_Data_M4_Price \
        Charts_Data_M5_Monthly \
        Charts_Data_M6 \
        Charts_Data_M10 \
        Charts_Data_M11 \
        Charts_Data_M12_Local_Fuel \
        Charts_Data_M12_Transportation \
        Charts_Data_M13 \
        Charts_Data_M14 \
        Charts_Data_M15 \
        Charts_Data_M16
}

function run_dashboard() {
    run_worksheets \
        Dashboard_M1 \
        Dashboard_M2_Annual \
        Dashboard_M2_Imports_Data \
        Dashboard_M2_Monthly \
        Dashboard_M3 \
        Dashboard_M4_Cost_Annual \
        Dashboard_M4_Cost_Monthly \
        Dashboard_M4_Price_Annual \
        Dashboard_M4_Price_Monthly \
        Dashboard_M5_Cost_Monthly \
        Dashboard_M5_Price_Annual \
        Dashboard_M5_Price_Monthly \
        Dashboard_M6_Quarterly \
        Dashboard_M8 \
        Dashboard_M8_Alt \
        Dashboard_M10_RPS \
        Dashboard_M11_EEPS \
        Dashboard_M11_HCEI \
        Dashboard_M12_Local_Fuel \
        Dashboard_M12_Transportation \
        Dashboard_M13 \
        Dashboard_M14 \
        Dashboard_M15 \
        Dashboard_M16_EEPS
}


run_dashboard
run_charts


