import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}
    name = 'testApiTanya'

    @allure.step('Check response status code')
    def check_that_status(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check response values')
    def check_response_data_is_correct(self, param, value):
        assert self.response.json()[param] == value

    @allure.step('Check the token is alive')
    def check_response_token_is_alive(self):
        assert self.response.text == f'Token is alive. Username is {self.name}'

    @allure.step('Check the token is delete')
    def check_response_delete_token(self, meme_id):
        assert self.response.text == f'Meme with id {meme_id} successfully deleted'


    @allure.step('Check response values')
    def check_response_data_is_not_empty(self):
       data = self.response.json()['data']
       if data:
           assert data[0]['id'] is not None