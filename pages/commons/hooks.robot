*** Settings ***
Library     Browser

Resource    ../../config/config.robot

*** Keywords ***
Start Clash Robot
    New Browser    ${BROWSER}    headless=false
    New Context    viewport={'width': ${SCREEN_WIDTH}, 'height': ${SCREEN_HEIGHT}}
    New Page       ${BASE_URL}

End Clash Robot
    Take Screenshot
    Close Browser