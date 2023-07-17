import http

import requests
from requests import exceptions
from src.infra.constants import URI_BRASILAPI


class Apibrazil:
    def get(self, url):
        try:
            return_call = requests.get(url=URI_BRASILAPI)

            if return_call.status_code != http.HTTPStatus.ACCEPTED:
                return None
            return return_call.json()
        except (exceptions.ConnectionError, exceptions.RequestException, exceptions.Timeout) as error:
            raise error