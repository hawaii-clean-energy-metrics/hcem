#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HCEMINITDIR="$(cd "${BASEDIR}/../010-init" && pwd)"
source ${HCEMINITDIR}/sourceme
IFS=$'\n'
CKANHEPF="${BASEDIR}/ckan_hcem_helper.py"
export CONFIG="${BASEDIR}/config.ini"

function create_or_update() {
    NAME=$1
    FILENAME=$2
    PACKAGEID=$3

    SEARCH_RESULTS=$("${CKANHEPF}" --command=resource_search --query=name:"${NAME}")
    COUNT=$(echo "${SEARCH_RESULTS}" | jq -r .count)
    if [[ "${COUNT}" == "0" ]]
    then
        upload_if_not_exists $1 $2 $3
        return
    fi
    if [[ "${COUNT}" != "1" ]]
    then
        echo
        echo "*****"
        echo "Found multiple entries: $NAME"
        echo "*****"
        return
    fi

        
    RESOURCE_ID=$(echo "${SEARCH_RESULTS}" | jq -r .results[0].id)
    if [[ ! -e "${FILENAME}" ]]
    then
        echo "file not found: ${FILENAME}"
        return
    fi

    echo "+++ updating ${FILENAME} as '${NAME}' to CKAN package '${PACKAGEID}'"
    "${CKANHEPF}" \
        --command=resource_update \
        --name="${NAME}" \
        --filename="${FILENAME}" \
        --id="${RESOURCE_ID}"
    sleep 1s
}


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
    XLSX="${FILEBASE}.xlsx"
    DATESTR=$(echo ${FILEBASE} | rev | cut -d_ -f1 | rev)
    FILENAME_CSV="${WORKSHEET_DIR}/${CSV}"
    FILENAME_XLSX="${WORKSHEET_DIR}/${XLSX}"

    NAMEBASE=$(echo "${FILEBASE::-20}" | tr _ \  ) # strip off datestamp and replace underscores with spaces
    create_or_update "$NAMEBASE CSV" "${FILENAME_CSV}" "${PACKAGEID}"
    create_or_update "$NAMEBASE XLSX" "${FILENAME_XLSX}" "${PACKAGEID}"
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

