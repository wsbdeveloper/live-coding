
from unittest.mock import patch

import pytest
from api_module import get_data_from_api


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # Neste exemplo, retornamos um dicionário simples como resposta da API
    # Mas você pode modificar de acordo com a estrutura real da resposta da API.
    return MockResponse({"key": "value"}, 200)

def test_get_data_from_api():
    # Usamos o patch para substituir temporariamente o requests.get pelo nosso mocked_requests_get
    with patch('api_module.requests.get', side_effect=mocked_requests_get):
        data = get_data_from_api()
    
    # Agora podemos testar o comportamento da função como se tivesse obtido a resposta real da API.
    assert data == {"key": "value"}