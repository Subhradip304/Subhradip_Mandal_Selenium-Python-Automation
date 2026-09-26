*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${URL}        https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}    Edge

*** Test Cases ***
Practice Waits And Synchronization
    Open Browser                 ${URL}                            ${BROWSER}
    Maximize Browser Window

    Wait Until Page Contains     Practice Page                     10s

    Wait Until Element Is Visible     id=name                      10s
    Input Text                   id=name                           subhradip

    Wait Until Element Is Enabled     id=name                      10s

    Wait Until Element Is Visible     xpath=//input[@value='radio2']    10s
    Click Element                xpath=//input[@value='radio2']

    Wait Until Element Is Visible     id=dropdown-class-example    10s
    Select From List By Value    id=dropdown-class-example         option2

    Wait Until Element Is Visible     id=checkBoxOption1           10s
    Select Checkbox              id=checkBoxOption1

    Sleep                        2s

    Close Browser
