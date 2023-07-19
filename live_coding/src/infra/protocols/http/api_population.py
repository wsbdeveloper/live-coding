import http

import requests
from requests import exceptions

from live_coding.src.infra.constants import URI_IBGE


class ApiIBGE:
    def get(self):
        try:
            ibge_data_response = requests.get(url=URI_IBGE)

            if ibge_data_response.status_code != http.HTTPStatus.OK.value:
                return None
            
            response = ibge_data_response.json()
            return response
        except (exceptions.ConnectionError, exceptions.RequestException, exceptions.Timeout) as error:
            raise error