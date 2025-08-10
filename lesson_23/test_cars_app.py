import pytest
import requests
import logging

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("search_test")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.fixture(scope="class")
def auth_token():
    login_data = {"username": "admin", "password": "admin"}
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    assert response.status_code == 200, "Login failed"
    token = response.json().get("access_token")
    assert token is not None, "No access token received"
    return token


@pytest.mark.usefixtures("auth_token")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 3),
        ("year", 5),
        ("mileage", 2),
        ("price", 1),
        ("year", 10),
        ("mileage", 5),
    ])
    def test_search_cars(self, auth_token, sort_by, limit):
        headers = {"Authorization": f"Bearer {auth_token}"}
        params = {"sort_by": sort_by, "limit": limit}

        response = requests.get(f"{BASE_URL}/search", headers=headers, params=params)

        logger.info(f"Запит: sort_by={sort_by}, limit={limit}")
        logger.info(f"Статус: {response.status_code}")
        logger.info(f"Відповідь: {response.json()}")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= limit
