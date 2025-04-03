import pytest
from constants import BASE_URL


class TestItems:
    endpoint = f"{BASE_URL}/items/"

    def test_create_item(self, item_data, new_item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (
            200,
            201,
        ), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]

        self.created_item_id = item_id

        change_item = auth_session.put(f"{self.endpoint}{item_id}", json=new_item_data)
        assert (
            change_item.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"

        delete_item = auth_session.delete(f"{self.endpoint}{item_id}")
        assert (
            delete_item.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert (
            response.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"
