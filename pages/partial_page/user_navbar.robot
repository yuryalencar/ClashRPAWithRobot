*** Settings ***
Resource    ../../components/components.robot

*** Keywords ***
Go To My Account
    Log To Console      user_navbar: Openning my account

    Click               ${USER_NAVBAR_TOOGLE}
    
    Wait For Elements State     css=${USER_NAVBAR_ACCOUNT_CSS_SELECTOR}   attached
    Execute Javascript          document.querySelector('${USER_NAVBAR_ACCOUNT_CSS_SELECTOR}').click()
