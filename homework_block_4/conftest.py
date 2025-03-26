import pytest, requests
from faker import Faker
from constants import HEADERS, BASE_URL


faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(
        f"{BASE_URL}/auth",
        headers=HEADERS,
        json={"username": "admin", "password": "password123"},
    )
    assert response.status_code == 200, "Ошибка авторизации"

    token = response.json().get("token")
    assert token is not None, "Токен не получен"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture()
def booking_data():
    return {
        "firstname": "faker.first_name()",
        "lastname": "faker.last_name()",
        "totalprice": faker.random_int(min=100, max=100_000),
        "depositpaid": True,
        "bookingdates": {"checkin": "2013-02-23", "checkout": "2014-10-23"},
        "additionalneeds": "Breakfast",
    }
