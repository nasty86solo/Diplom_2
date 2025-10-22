import allure
import pytest
from src.data import Status
from src.factories import user_payload

@allure.suite("Users")
class TestUsers:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, registered_user):
        response = registered_user["response"]
        body = response.json()
        assert response.status_code in (Status.OK, Status.CREATED)
        assert body.get("success") is True
        assert "accessToken" in body

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, users, registered_user):
        first = registered_user["response"]
        payload = registered_user["payload"]
        assert first.status_code in (Status.OK, Status.CREATED)

        dup = users.register(payload)
        assert dup.status_code in (Status.FORBIDDEN, Status.CONFLICT)
        assert ("message" in dup.json()) or ("error" in dup.text)

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize("missing", ["email", "password", "name"])
    def test_create_user_missing_required(self, users, missing):
        payload = user_payload()
        payload[missing] = "" 
        r = users.register(payload)
        assert r.status_code in (Status.FORBIDDEN, Status.BAD_REQUEST)
        assert ("message" in r.json()) or ("error" in r.text)
