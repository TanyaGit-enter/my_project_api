import requests
import allure

from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):

    @allure.step('Put meme_id')
    def put_meme_id(self, meme_id, payload, headers=None):
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=headers
        )
        return self.response
