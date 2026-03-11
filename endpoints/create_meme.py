from http import HTTPStatus

import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    meme_id = None

    @allure.step('Create new meme')
    def create_new_meme(self, payload, headers=None):
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers=headers

        )
        if self.response.status_code == HTTPStatus.OK:
            self.meme_id = self.response.json()['id']
        return self.response
