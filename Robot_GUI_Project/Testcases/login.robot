*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            http://www.amazon.in/
${BROWSER}        Chrome

*** Test Cases ***
verify login Functionality
    Open Browser    ${URL}    ${browser}
    Maximize Browser Window
    sleep    10s
    Input Text    id=twotabsearchtextbox    laptop
    sleep    10s
    Click Element    id=nav-search-submit-button
   # press Key    id=nav-search-submit-button    ENTER