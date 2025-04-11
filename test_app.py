import pytest

from app import app


@pytest.fixture(name="client")
def fixture_client():
    with app.test_client() as client:
        yield client


def test_add(client):
    response = client.post("/api/add", json={"a": 5, "b": 3})
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["sum"] == 8
