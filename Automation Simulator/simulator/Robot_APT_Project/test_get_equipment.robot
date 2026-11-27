*** Settings***
Library     RequestsLibrary
 
***Variables***
${BASE_URL}     http://127.0.0.1:5005
 
***Test Cases ***
Test Get All Equipment
    Create Session      Equipment_API       ${BASE_URL}
    ${response}=       GET On Session      Equipment_API       /api/equipment
    Should Be Equal As Integers     ${response.status_code}     200
    Log to Console      ${response.json()}