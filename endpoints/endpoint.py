import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    response = None
    json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Check response status code')
    def check_that_status(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Check response values')
    def check_response_data_is_correct(self, param, value):
        assert self.response.json()[param] == value
