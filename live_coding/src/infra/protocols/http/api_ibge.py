import http

import requests
from requests import exceptions
from src.infra.constants import API_IBGE


class Apibrazil:
    def get(self):
        try:
            return_call = requests.get(url=API_IBGE)

            if return_call.status_code != http.HTTPStatus.ACCEPTED:
                return None
            return return_call.json()
        except (exceptions.ConnectionError, exceptions.RequestException, exceptions.Timeout) as error:
            raise error