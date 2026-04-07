import requests
import allure

from endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Put meme_id')
    def delete_meme_id(self, meme_id, headers=None):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        return self.response
