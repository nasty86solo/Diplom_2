from typing import Dict, Any, List
import allure
from .http import ApiClient
from .urls import ORDERS, INGREDIENTS 

class OrdersApi:
    def __init__(self, client: ApiClient) -> None:
        self.client = client

    @allure.step("Create order via /api/orders")
    def create(self, payload: Dict[str, Any], authorized: bool=False):
        return self.client.post(ORDERS, json=payload, auth=authorized)

    @allure.step("Fetch ingredients via /api/ingredients")
    def list_ingredients(self) -> List[str]:
        r = self.client.get(INGREDIENTS)
        r.raise_for_status()
        body = r.json()
        ids = [item.get('_id') for item in body.get('data', []) if item.get('_id')]
        return ids
