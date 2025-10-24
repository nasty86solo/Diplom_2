import os
import sys

import pytest

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.http import ApiClient
from src.users import UsersApi
from src.orders import OrdersApi

@pytest.fixture(scope="session")
def client() -> ApiClient:

    c = ApiClient()
    return c

@pytest.fixture()
def users(client: ApiClient) -> UsersApi:
    return UsersApi(client)

@pytest.fixture()
def orders(client: ApiClient) -> OrdersApi:
    return OrdersApi(client)

@pytest.fixture()
def registered_user(users: UsersApi):
    payload, response = users.register_unique_user()
    token = response.json().get("accessToken")
    context = {"payload": payload, "token": token, "response": response}
    yield context
    token_value = context.get("token")
    if token_value:
        users.client.set_token(token_value)
        users.delete_current()
        users.client.set_token(None)

@pytest.fixture()
def created_user_token(registered_user):
    return registered_user.get("token")

@pytest.fixture()
def auth_token(users: UsersApi):
    payload, _ = users.register_unique_user()
    resp_login = users.login(payload["email"], payload["password"])
    resp_login.raise_for_status()
    token = resp_login.json().get("accessToken")
    yield token
    if token:
        users.client.set_token(token)
        users.delete_current()
        users.client.set_token(None)
