*** Settings ***
Library     RequestsLibrary
 
*** Variables   ***
${BASE_URL}     http://127.0.0.1:5001
 
 
***Keywords***
Create_API_Session
        Create Session      Equipment_API      ${BASE_URL}
 
Get All Equipment
    ${response}=    GET on Session     Equipment_API        /api/equipment      expected_status=200
    RETURN      ${response}

Get Equipment by id
    [Arguments]     ${equipment_id}     ${equipment_status}
    ${response}=        GET On Session      Equipment_API       /api/equipment/${equipment_id}      expected_status=${equipment_status}
    RETURN      ${response}