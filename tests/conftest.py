import pytest
from fastapi.testclient import TestClient



@pytest.fixture
def client():
    from app.main import app
    app = TestClient(app)
    return app

