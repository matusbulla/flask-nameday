from datetime import date
from unittest.mock import patch

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_nameday(client):
    with patch("app.date") as mock_date:
        mock_date.today.return_value = date(2026, 4, 24)
        mock_date.side_effect = lambda *args, **kwargs: date(*args, **kwargs)
        response = client.get("/")

    assert response.status_code == 200
    data = response.get_json()
    assert data["date"] == "2026-04-24"
    assert data["name"] == "Juraj"


def test_index_multiple_names(client):
    with patch("app.date") as mock_date:
        mock_date.today.return_value = date(2026, 6, 29)
        mock_date.side_effect = lambda *args, **kwargs: date(*args, **kwargs)
        response = client.get("/")

    data = response.get_json()
    assert data["name"] == "Peter, Pavol, Petra"
