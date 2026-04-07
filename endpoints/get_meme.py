import requests
import allure

from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.step('Get meme with id')
    def get_meme_id(self, meme_id, headers=None):
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        # print(self.response)
        return self.response

    @allure.step('Get all memes')
    def get_all_memes(self, headers=None):
        self.response = requests.get(
            f'{self.url}/meme',
            headers=headers
        )
        print(self.response)
        return self.response
