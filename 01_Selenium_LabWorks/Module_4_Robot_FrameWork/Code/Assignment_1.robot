*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://rahulshettyacademy.com/AutomationPractice/
${BROWSER}    Chrome

*** Test Cases ***
Verify Automation Practice Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Practice Page
    Close Browser
