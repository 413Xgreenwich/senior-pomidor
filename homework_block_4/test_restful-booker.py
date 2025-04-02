import pytest
import requests
from constants import BASE_URL


class TestBookings:

    def test_create_booking(self, auth_session, booking_data, new_booking_data, partial_booking_data):

        health_check = auth_session.get(f"{BASE_URL}/ping")
        assert health_check.status_code == 201, "Сервер не доступен"

        get_all_bookings = auth_session.get(f"{BASE_URL}/booking")
        assert get_all_bookings.status_code == 200, "Данные о бронях не получены"
        assert len(get_all_bookings.json()) != 0, "Данные о бронях не получены"

        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "Идентификатор брони не найден в ответе"
        assert (
            create_booking.json()["booking"]["firstname"] == booking_data["firstname"]
        ), "Заданное имя не совпадает с полученным"
        assert (
            create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"]
        ), "Заданная стоимость не совпадает с полученной"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert (
            get_booking.json()["lastname"] == booking_data["lastname"]
        ), "Заданная фамилия не совпадает с полученной"

        put_update_booking = auth_session.put(
            f"{BASE_URL}/booking/{booking_id}", json=new_booking_data
        )
        assert (
            put_update_booking.json()["firstname"] == new_booking_data["firstname"]
        ), "Поле firstname не совпадает с ожидаемым"
        assert (
            put_update_booking.json()["lastname"] == new_booking_data["lastname"]
        ), "Поле lastname не совпадает с ожидаемым"

        patch_update_booking = auth_session.patch(
            f"{BASE_URL}/booking/{booking_id}", json=partial_booking_data
        )
        assert (
            patch_update_booking.json()["additionalneeds"]
            == partial_booking_data["additionalneeds"]
        ), "Поле additionalneeds не совпадает с ожидаемым"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалилась"
