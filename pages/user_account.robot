*** Settings ***
Library     ../libs/get_my_ip.py

Resource    ./partial_page/user_navbar.robot

*** Keywords ***
Generate an New Key
    Click       ${USER_NEW_KEY_BUTTON}

    Type Text   ${USER_KEY_NAME_INPUT}          Example Key Name           clear=True
    Type Text   ${USER_DESCRIPTION_TEXTAREA}    Example Key Description    clear=True

    ${machine_ip}    Get This External Machine Ip
    Type Text       ${USER_FIRST_IP}        ${machine_ip}       clear=True

    click       ${BUTTON_SUBMIT}