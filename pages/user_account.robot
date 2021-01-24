*** Settings ***
Library     ../libs/get_my_ip.py
Library     ../libs/csv_manipulations.py

Resource    ./partial_page/user_navbar.robot

*** Keywords ***
Generate an New Key
    Click       ${USER_NEW_KEY_BUTTON}

    Type Text   ${USER_KEY_NAME_INPUT}          Example Key Name           clear=True
    Type Text   ${USER_DESCRIPTION_TEXTAREA}    Example Key Description    clear=True

    ${machine_ip}    Get This External Machine Ip
    Type Text       ${USER_FIRST_IP}        ${machine_ip}       clear=True

    Click       ${BUTTON_SUBMIT}

Create CSV With "${clan_name}" of the Brazil Clan informations
    Click       ${USER_TITLE_API_KEY}
    ${token}    Get Text                    ${USER_FIRST_API_KEY}

    Make Clan Informations Csv    ${token}    ${BASE_API_URL}    ${clan_name}    ${BRAZIL_LOCATION_ID}      ${TAG_CLA_START}