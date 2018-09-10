#!/bin/bash
set -ex
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

DATESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
DESTBASEDIR="${BASEDIR}/../050-Automated_Input_Data"


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
       echo "same...deleting ${2}"
       rm ${2}
    else
        echo "different...keeping ${2}"
    fi
}


function init_dir() {
    DESTDIR="${DESTBASEDIR}/${1}"
    DEST="${DESTDIR}/${1}_${DATESTAMP}.csv"
    mkdir -p "${DESTDIR}"
    OLD_FILE=$(ls -1 ${DESTDIR}/${1}_????-??-??-??-??-??.csv | tail -1)
    echo "DESTDIR=${DESTDIR}"
    echo "DEST=${DEST}"
    echo "OLD_FILE=${OLD_FILE}"
}


function getxl() {
    init_dir ${1}
    shift

    echo "Grabbing ${DEST} from ${*}"

    ${BASEDIR}/Spreadsheet.py ${*} > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_eia_petroleum() {
    init_dir ${1}
    shift
    EIA_PETROLEUM_BASE_URL="http://www.eia.gov/petroleum/imports/companylevel/archive/"
    URL="${EIA_PETROLEUM_BASE_URL}"
    echo "Grabbing ${DEST} from ${URL}"

    cd "${DESTDIR}"
    wget --no-verbose --no-clobber -r -l1 -q --progress=bar --no-parent -A "*.xls,*.xlsx" "${URL}"
    cd "${BASEDIR}"

    echo "Extracting excel files to csv..."
    find "${DESTDIR}" -name "*.xls" -or -name "*.xlsx" | sort | grep -v _prel | xargs ${BASEDIR}/eia_petroleum.py > "${DEST}"
    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_epa_co2_emissions() {
    init_dir ${1}
    shift

    "${BASEDIR}"/epa_co2_emissions_hawaii.py > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_eia_seds() {
    init_dir ${1}
    shift

    EIA_SEDS_CSV="Complete_SEDS.csv"

    #URL_BASE_EIA_SEDS="https://www.eia.gov/state/seds/seds-data-fuel.php"
    #LINKS=$("${BASEDIR}"/links_in_url.py "${URL_BASE_EIA_SEDS}")
    #URL_SEDS_CSV=$(echo "${LINKS}" | grep csv | grep Complete | head -1)
    #URL_SEDS_CODES=$(echo "${LINKS}" | grep xlsx | grep Codes | head -1)


    URL_SEDS_CSV="https://www.eia.gov/state/seds/CDF/Complete_SEDS.csv"
    URL_SEDS_CODES="https://www.eia.gov/state/seds/CDF/Codes_and_Descriptions.xlsx"

    FILE_SEDS_CSV="${DESTDIR}/Complete_SEDS.csv"
    FILE_SEDS_CODES="${DESTDIR}/Codes_and_Descriptions.xlsx"

    echo "URL_SEDS_CSV=${URL_SEDS_CSV}"
    echo "URL_SEDS_CODES=${URL_SEDS_CODES}"
    wget --no-verbose -L "${URL_SEDS_CSV}" -O "${FILE_SEDS_CSV}"
    wget --no-verbose -L "${URL_SEDS_CODES}" -O "${FILE_SEDS_CODES}"

    ${BASEDIR}/eia_seds.py "${FILE_SEDS_CSV}" "${FILE_SEDS_CODES}" > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_eia_foreign_coal() {
    init_dir ${1}
    shift

    "${BASEDIR}"/EIA_Imports_Coal_Foreign.py > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_dbedt_population() {
    init_dir ${1}
    shift

    "${BASEDIR}"/dbedt_population.py > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}


function process_gsp_hi() {

    ZIPFILE=GDPState.zip
    CSVFILE=gdpstate_naics_HI.csv
    URL_ZIPFILE="https://apps.bea.gov/regional/zip/gdpstate/GDPState.zip"

    init_dir ${1}
    shift

    cd "${DESTDIR}"
    wget --no-verbose -L "${URL_ZIPFILE}" -O "${ZIPFILE}"
    unzip -o "${ZIPFILE}" "${CSVFILE}"
    cd "${BASEDIR}"
    "${BASEDIR}"/GSP.py "${DESTDIR}/${CSVFILE}" > "${DEST}"

    compare_and_delete_if_same "${OLD_FILE}" "${DEST}"
}

getxl RPS 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRSatJbu2opk5WXaO9qY6OiYcgFTjCFZwQUq4yrVtkkWR3kGQwqz32Jb2zrl_9gaAxscbN3KyfO3IkR/pub?gid=1165316079&single=true&output=csv&extensionForSpreadsheet.py.hack=.csv' 0 0

getxl DBEDT_Monthly_Energy http://files.hawaii.gov/dbedt/economic/data_reports/energy-trends/Monthly_Energy_Data.xlsx 0 0
getxl EIA_Crude_WTI https://www.eia.gov/dnav/pet/hist_xls/RWTCm.xls -1 1
getxl EIA_Crude_Europe_Brent https://www.eia.gov/dnav/pet/hist_xls/RBRTEm.xls -1 1
getxl EIA_Propane_Price https://www.eia.gov/dnav/pet/hist_xls/EER_EPLLPA_PF4_Y44MB_DPGm.xls -1 1
getxl EIA_Fuel_Oil_Price http://www.eia.gov/dnav/pet/hist_xls/EMA_EPPR_PWG_NUS_DPGm.xls -1 1
getxl EIA_Jet_Fuel_Price https://www.eia.gov/dnav/pet/hist_xls/EER_EPJK_PF4_RGC_DPGm.xls -1 1

getxl GSP_Deflator 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=A191RD3A086NBEA'

# EIA_Existing Capcity / source https://www.eia.gov/electricity/data/state/
getxl EIA_Existing_Capacity https://www.eia.gov/electricity/data/state/existcapacity_annual.xls

process_gsp_hi GSP


# https://www.epa.gov/statelocalclimate/state-energy-co2-emissions
process_epa_co2_emissions EPA_CO2_Emissions

# https://www.eia.gov/state/seds/seds-data-complete.cfm
process_eia_seds EIA_SEDS

# http://www.eia.gov/coal/distribution/quarterly/
# http://www.eia.gov/coal/distribution/annual/
# http://www.eia.gov/coal/distribution/annual/archive.php
process_eia_foreign_coal EIA_Imports_Coal_Foreign

process_eia_petroleum EIA_Imports_Petroleum

process_dbedt_population DBEDT_Population
