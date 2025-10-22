import requests
from typing import Optional, Dict, Any
from .config import BASE_URL

class ApiClient:
    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url
        self.session = requests.Session()
        self._auth_token: Optional[str] = None

    def set_token(self, token: Optional[str]) -> None:
        self._auth_token = token
        if token is None:
            # Clear session cookies so further unauthenticated calls do not reuse auth cookies.
            self.session.cookies.clear()

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers: Dict[str, str] = {}
        if self._auth_token:
            headers["Authorization"] = self._auth_token
        if extra:
            headers.update(extra)
        return headers

    def post(self, path: str, json: Optional[Dict[str, Any]] = None, auth: bool=False, headers: Optional[Dict[str,str]]=None):
        return self.session.post(self.base_url + path, json=json, headers=self._headers(headers) if auth else headers)

    def get(self, path: str, params: Optional[Dict[str, Any]] = None, auth: bool=False, headers: Optional[Dict[str,str]]=None):
        return self.session.get(self.base_url + path, params=params, headers=self._headers(headers) if auth else headers)

    def delete(self, path: str, auth: bool=True, headers: Optional[Dict[str,str]]=None):
        return self.session.delete(self.base_url + path, headers=self._headers(headers) if auth else headers)
