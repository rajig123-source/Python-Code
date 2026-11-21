import pytest
from app import app
 
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
 
def test_get_equipment(client):
    response = client.get('/api/equipment')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]['id'] == 101
    assert data[0]['name'] == "Flight control unit"
    assert data[0]['type'] == "FCU"
    assert data[0]['status'] == "Operational"
    assert data[1]['id'] == 102
    assert data[1]['name'] == "Navigation System"
    assert data[1]['type'] == "NS"
    assert data[1]['status'] == "Operational"
    assert data[2]['id'] == 103
    assert data[2]['name'] == "Flight Management System" 
    assert data[2]['type'] == "FMS"
    assert data[2]['status'] == "Operational"
 
@pytest.mark.parametrize("equipment_id, name, type, status, expected_status_code", [
    (101, "Flight control unit", "FCU", "Operational", 200),
    (102, "Navigation System", "NS", "Operational", 200),
    (103, "Flight Management System", "FMS", "Operational", 200),
    (999, None, None, None, 404),  # Non-existent equipment ID
])
def test_get_equipment_by_id(client, equipment_id, name, type, status, expected_status_code):
    response = client.get(f'/api/equipment/{equipment_id}')
    assert response.status_code == expected_status_code
    if expected_status_code == 200:
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 1
        assert data[0]['id'] == equipment_id
        assert data[0]['name'] == name
        assert data[0]['type'] == type
        assert data[0]['status'] == status
    else:
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == "Equipment not found"