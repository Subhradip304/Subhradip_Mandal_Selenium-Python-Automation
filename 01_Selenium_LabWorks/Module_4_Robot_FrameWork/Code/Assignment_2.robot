*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}    Chrome

*** Test Cases ***
Handle Web Elements
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id=name    Subhradip

    Select Radio Button    radioButton    radio2

    Select From List By Value    id=dropdown-class-example    option2

    Select Checkbox    id=checkBoxOption1

    Sleep    2s

    Close Browser
