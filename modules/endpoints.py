from modules.common import api as _api
from configurations.api_configs import api_configs as _api_configs

from requests import Response


class Endpoints:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Endpoints, cls).__new__(cls)
        return cls._instance

    def __init__(self, env: str):
        self._configs = _api_configs[env]
        self._base_url = self._configs['base_url']
        self._paths = self._configs['paths']

    @property
    def users(self) -> Response:
        _url = self._base_url + self._paths['users']
        response = _api.get(url=_url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(response.status_code, response.text)

    @property
    def todos(self) -> Response:
        _url = self._base_url + self._paths['todos']
        response = _api.get(url=_url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(response.status_code, response.text)
