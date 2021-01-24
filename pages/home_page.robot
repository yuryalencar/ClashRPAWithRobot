*** Settings ***
Resource    ../components/components.robot

*** Keywords ***
Make Login Using Default User
    Wait For Elements State     css=${HOME_NAVBAR_LOGIN_CSS_SELECTOR}   attached
    Execute Javascript          document.querySelector("${HOME_NAVBAR_LOGIN_CSS_SELECTOR}").click()

    Type Text   ${HOME_EMAIL_INPUT}         ${DEFAULT_USER}         clear=True
    Type Text   ${HOME_PASSWORD_INPUT}      ${DEFAULT_PASSWORD}     clear=True

    Click       ${BUTTON_SUBMIT}