from typing import Dict, Any
import allure
from .http import ApiClient
from .urls import AUTH_REGISTER, AUTH_LOGIN, AUTH_USER
from .factories import user_payload

class UsersApi:
    def __init__(self, client: ApiClient) -> None:
        self.client = client

    @allure.step("Register user via /api/auth/register")
    def register(self, payload: Dict[str, Any]):
        return self.client.post(AUTH_REGISTER, json=payload)

    @allure.step("Login user via /api/auth/login")
    def login(self, email: str, password: str):
        return self.client.post(AUTH_LOGIN, json={"email": email, "password": password})

    @allure.step("Delete current user via /api/auth/user")
    def delete_current(self):
        # Требует Authorization токен
        return self.client.delete(AUTH_USER, auth=True)

    @allure.step("Register unique user with retry on conflict")
    def register_unique_user(self):
        payload = user_payload()
        response = self.register(payload)
        if response.status_code in (403, 409):
            payload = user_payload()
            response = self.register(payload)
        response.raise_for_status()
        return payload, response
