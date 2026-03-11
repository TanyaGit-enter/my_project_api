from endpoints.endpoint import Endpoint
import requests


class CreateToken(Endpoint):
    _token = None

    def get_token(self):
        if self._token is None:
            self._token = self.create_new_token()
        return self._token

    def create_new_token(self):
        self.response = requests.post(f'{self.url}/authorize', json={"name": "testApiTanya"})
        return self.response.json()['token']

    def refresh_token(self):
        self.response = self.create_new_token()
        return self.response
