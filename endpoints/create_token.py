from http import HTTPStatus

from endpoints.endpoint import Endpoint
import requests


class CreateToken(Endpoint):
    _token = None

    def get_token(self):
        if self._token is None:
            self._token = self.create_new_token()
        return self._token

    def create_new_token(self, payload=Endpoint.name):
        self.response = requests.post(f'{self.url}/authorize', json=payload)
        if self.response.status_code == HTTPStatus.OK:
            return self.response.json()['token']
        else:
            return self.response
