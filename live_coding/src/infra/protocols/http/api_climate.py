import http

import requests
from requests import exceptions

from live_coding.src.infra.constants import URI_BRASILAPI


class Apibrazil:
    def get(self):
        try:
            return_call = requests.get(url=URI_BRASILAPI)

            if return_call.status_code != http.HTTPStatus.OK.value:
                return None
            
            response = return_call.json()
            
            return response
        except (exceptions.ConnectionError, exceptions.RequestException, exceptions.Timeout) as error:
            raise error