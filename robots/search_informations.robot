*** Settings ***
Resource        ../config/page_register.robot

Test Setup      Start Clash Robot
Test Teardown   End Clash Robot

*** Test Cases ***
Create an New Key
    Make Login Using Default User
    Go To My Account
    Generate an New Key
    Sleep       6