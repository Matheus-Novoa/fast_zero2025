import pytest
from fastapi.testclient import TestClient

from fast_zero2025.app import app


@pytest.fixture
def client():
    return TestClient(app)
