import pytest
import xdist 
from app import app
import threading
 
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
         yield client
 
@pytest.mark.parametrize("equipment_id", [101, 102])
def test_get_equipment_by_id(client, equipment_id):
    print("Test 1 started")
    response = client.get(f"/api/equipment/{equipment_id}")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert data["id"] == equipment_id
def test_get_all_equipment(client):
    print("Test 2 started")
    response = client.get(f'api/equipment')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert len(data) == 2
    assert data[0]["id"] == 101
    assert data[0]["name"] == "Flight control unit"
    assert data[0]["type"] == "FCU"
    assert data[0]["status"] == "Operational"
    assert data[1]["id"] == 102
    assert data[1]["name"] == "Navigation System"
    assert data[1]["type"] == "NS"
    assert data[1]["status"] == "Operational"
 