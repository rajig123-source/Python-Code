*** Settings***
Library     RequestsLibrary
 
***Variables***
${BASE_URL}     http://127.0.0.1:5001
 
***Keywords***
 Create API Session
    Create Session      Equipment_API       ${BASE_URL}
***Test Cases ***
TC001_Test Get All Equipment
    Create  API Session
    ${response}=        GET On Session      Equipment_API       /api/equipment
    Should Be Equal As Integers     ${response.status_code}     200
    Log to Console      ${response.json()}
TC002_Test_GET_One
    Create Session      Equipment_API       ${BASE_URL}
    ${response}=        GET On Session      Equipment_API       /api/equipment/101
    Should Be Equal As Integers     ${response.status_code}     200
    ${data}=        Set Variable       ${response.json()}
    #Should be Equal As Integers     ${data}[id]     101
    Should be Equal As Strings      ${data}[name]     Flight control unit
    Should be Equal As Strings      ${data}[type]     FCU
    Should be Equal As Strings      ${data}[status]     Operational
   # Log to Console      ${response.json()}
    Log to Console      All Equipment Details: ${data}
