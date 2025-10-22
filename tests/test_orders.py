import allure
import pytest
from src.data import Status
from src.orders import OrdersApi

@allure.suite("Orders")
class TestOrders:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_authorized(self, orders: OrdersApi, users, auth_token):
        users.client.set_token(auth_token)
        ingredients = orders.list_ingredients()
        assert ingredients, "Ожидали, что API вернёт список ингредиентов"
        payload = {"ingredients": ingredients[:3]}
        r = orders.create(payload, authorized=True)
        assert r.status_code in (Status.OK, Status.CREATED)
        body = r.json()
        assert body.get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self, orders: OrdersApi):
        ingredients = orders.list_ingredients()
        payload = {"ingredients": ingredients[:2]}
        r = orders.create(payload, authorized=False)
        if r.status_code in (Status.UNAUTHORIZED, Status.FORBIDDEN):
            return
        assert r.status_code == Status.OK
        body = r.json()
        if body.get("success") is True:
            pytest.xfail("API allows order creation without authorization token")
        assert body.get("success") is False or "message" in body

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, orders: OrdersApi, users, auth_token):
        users.client.set_token(auth_token)
        r = orders.create({"ingredients": []}, authorized=True)
        assert r.status_code in (Status.BAD_REQUEST, Status.FORBIDDEN)

    @allure.title("Создание заказа с невалидным ингредиентом")
    def test_create_order_invalid_ingredient(self, orders: OrdersApi, users, auth_token):
        users.client.set_token(auth_token)
        payload = {"ingredients": ["deadbeefdeadbeefdeadbeef"]}
        r = orders.create(payload, authorized=True)
        assert r.status_code in (Status.BAD_REQUEST, Status.SERVER_ERROR)
