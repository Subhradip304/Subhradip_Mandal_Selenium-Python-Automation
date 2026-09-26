*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}    Chrome

*** Test Cases ***
Complete Automation Practice
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Wait Until Page Contains    Practice Page    10s

    Input Text    id=name    Subhradip

    Select Radio Button    radioButton    radio1

    Select From List By Value    id=dropdown-class-example    option2

    Select Checkbox    id=checkBoxOption1

    Element Should Be Visible    id=name
    Element Should Be Enabled    id=name

    Click Element    xpath=//input[@value='radio3']

    Capture Page Screenshot    assignment_6_final.png

    Close Browser
