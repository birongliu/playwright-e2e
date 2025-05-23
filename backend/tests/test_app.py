import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    yield


def test_read_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"health": "ok"}
