#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="$(cd "${BASEDIR}/../010-init" && pwd)"
source ${HCEMINITDIR}/sourceme
IFS=$'\n'
CKANHEPF="${BASEDIR}/ckan_hcem_helper.py"
export CONFIG="${BASEDIR}/config.ini"

function upload_if_not_exists() {
    NAME=$1
    FILENAME=$2
    PACKAGEID=$3

    COUNT=$("${CKANHEPF}" --command=resource_search --query=name:"${NAME}" | jq -r .count)
    if [[ ${COUNT} != "0" ]]
    then
        echo "${NAME} already exists in CKAN"
        return
    fi
    if [[ ! -e "${FILENAME}" ]]
    then
        echo "file not found: ${FILENAME}"
        return
    fi
    echo "+++ uploading ${FILENAME} as '${NAME}' to CKAN package '${PACKAGEID}'"
    "${CKANHEPF}" \
        --command=resource_create \
        --name="${NAME}" \
        --filename="${FILENAME}" \
        --package_id="${PACKAGEID}"
    sleep 1s
}

function upload_csv_and_xlsx() {
    CSV=$(basename "$1")
    WORKSHEET_DIR=$(dirname "$1")
    WORKSHEET=$(basename $WORKSHEET_DIR)
    cd "$WORKSHEET_DIR"
    METRICNUM=$(echo $WORKSHEET | grep -oPe '_M\K[0-9][0-9]?')
    PACKAGEID="hawaii-clean-energy-metric-${METRICNUM}"
    FILEBASE=$(basename "${CSV}" .csv)
    NAMEBASE=$(echo "${FILEBASE}" | tr _ \  )
    XLSX="${FILEBASE}.xlsx"
    DATESTR=$(echo ${FILEBASE} | rev | cut -d_ -f1 | rev)
    FILENAME_CSV="${WORKSHEET_DIR}/${CSV}"
    FILENAME_XLSX="${WORKSHEET_DIR}/${XLSX}"

    upload_if_not_exists "$NAMEBASE CSV" "${FILENAME_CSV}" "${PACKAGEID}"
    upload_if_not_exists "$NAMEBASE XLSX" "${FILENAME_XLSX}" "${PACKAGEID}"
    return

    IDS=$("${CKANHEPF}" --command=resource_search --query=name:"${NAMEBASE} XLSX" | jq -r .results[].id)
    if [[ -n "${IDS}" ]]
    then
        echo "$NAMEBASE already exists in CKAN"
        return
    fi
    "${CKANHEPF}" \
        --command=resource_create \
        --name="${NAMEBASE} XLSX" \
        --package_id="${PACKAGEID}" \
        --filename="${FILENAME_XLSX}" \
        --debug=True
    continue

    "${CKANHEPF}" \
        --command=resource_create \
        --name="${NAMEBASE} CSV" \
        --package_id="${PACKAGEID}" \
        --filename="${FILENAME_CSV}" \
        --debug=True

}

function scan_model_outputs_dir_and_upload()
{
    cd "${BASEDIR}/../060-Automated_Model_Outputs"
    WORKSHEETSDIR=${PWD}
    WORKSHEETSDIRS=$(ls -1d "${WORKSHEETSDIR}/"*${1}* | sort -V)
    for WORKSHEETDIR in $WORKSHEETSDIRS
    do
        WORKSHEET=$(basename $WORKSHEETDIR)
        cd "$WORKSHEETDIR"
        for CSV in ${WORKSHEET}_*.csv
        do
           upload_csv_and_xlsx "${WORKSHEETDIR}/${CSV}"
        done
    done
}


scan_model_outputs_dir_and_upload ${1}

# ID=$ID FILENAME="${FILENAME_CSV}" ${BASEDIR}/upload.py "${BASEDIR}/csv.ini"
# ID=$ID TITLE=Spreadsheet ${BASEDIR}/upload.py "${BASEDIR}/view_create_grid.ini"

