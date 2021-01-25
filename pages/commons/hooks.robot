*** Settings ***
Library     Browser

Resource    ../../config/config.robot

*** Keywords ***
Initialize Logs
    Log To Console  \n\n*********************************************************
    Log To Console  RPA SAMPLE USING CLASH ROYALE: START EXECUTION
    Log To Console  *********************************************************\n

Start Clash Robot
    Initialize Logs
    Log To Console  hooks: Running Start Clash Hooks

    New Browser     ${BROWSER}    headless=${HEADLESS}
    New Context     viewport={'width': ${SCREEN_WIDTH}, 'height': ${SCREEN_HEIGHT}}
    New Page        ${BASE_URL}

End Clash Robot
    Log To Console  hooks: Finishing Robot

    Take Screenshot
    Close Browser
    
    Log To Console  \n*********************************************************
    Log To Console  ROBOT EXECUTION FINALIZED
    Log To Console  *********************************************************\n