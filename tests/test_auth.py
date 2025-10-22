import allure
import pytest
from src.data import Status

@allure.suite("Auth")
class TestAuth:

    @allure.title("Логин под существующим пользователем")
    def test_login_ok(self, users, registered_user):
        payload = registered_user["payload"]
        resp = users.login(payload["email"], payload["password"])
        assert resp.status_code in (Status.OK, )
        body = resp.json()
        assert body.get("success") is True
        assert "accessToken" in body

    @allure.title("Логин с неверными данными")
    @pytest.mark.parametrize("email,password", [
        ("wrong_email@example.com", "correctpass"),
        ("correct_email@example.com", "wrongpass"),
    ])
    def test_login_invalid(self, users, email, password):
        resp = users.login(email, password)
        assert resp.status_code == Status.UNAUTHORIZED
        assert ("message" in resp.json()) or ("error" in resp.text)
