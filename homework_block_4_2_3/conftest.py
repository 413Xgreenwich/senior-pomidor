import pytest, requests
from faker import Faker
from constants import BASE_URL, AUTH_HEADERS, API_HEADERS, AUTH_DATA


fake = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(AUTH_HEADERS)

    response = requests.post(
        f"{BASE_URL}/login/access-token",
        headers=AUTH_HEADERS,
        data=AUTH_DATA,
    )
    assert response.status_code == 200, "Ошибка авторизации"

    token = response.json().get("access_token")
    assert token is not None, "Токен не получен"

    session.headers.update(API_HEADERS)
    session.headers.update({"authorization": f"Bearer {token}"})
    return session


@pytest.fixture()
def item_data():
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10),
    }
