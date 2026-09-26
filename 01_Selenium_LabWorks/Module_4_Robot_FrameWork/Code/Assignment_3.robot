*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}    Chrome

*** Test Cases ***
Practice Locators And XPath
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Input Text    id=name    Subhradip

    Select Radio Button    radioButton    radio1

    Select From List By Value    id=dropdown-class-example    option3

    Select Checkbox    xpath=//input[@value='option2']

    Click Element    xpath=//input[@value='radio3']

    Element Should Be Visible    xpath=//input[@id='name']

    Element Should Be Enabled    xpath=//input[@id='name']

    Close Browser
