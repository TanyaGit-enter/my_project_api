import allure

from endpoints.endpoint import Endpoint
import requests


class GetToken(Endpoint):

    @allure.step('Get token')
    def get_token(self, token_id=None):
        self.response = requests.get(f'{self.url}/authorize/{token_id}', headers=self.headers)
        return self.response
