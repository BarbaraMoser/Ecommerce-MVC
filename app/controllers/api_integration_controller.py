import json
from typing import Final

import requests


class CepApiIntegrationController:
    _BASE_URL: Final = 'https://viacep.com.br/ws/'
    _FORMAT: Final = '/json'

    @classmethod
    def find_address_by_cep(cls, cep: str):
        url_api = f'{cls._BASE_URL}{cep}{cls._FORMAT}'
        req = requests.get(url_api)
        if not req.status_code == 200:
            raise Exception('Endereço não encontrado')
        dados_json = json.loads(req.text)
        return dados_json
