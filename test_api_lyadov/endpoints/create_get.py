import requests
import allure
from endpoints.endpoint import Endpoint


class CreateGet(Endpoint):

    @allure.step('Вызов get запроса со всеми объектами')
    def challenge_all_obj(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Проверяем, что ответ содержит поле "data" и это список')
    def check_data_response(self):
        assert 'data' in self.json, \
            "Response doesn't contain 'data' field"
        assert isinstance(self.json['data'], list), \
            "'data' is not a list"

    @allure.step('Для каждого объекта в data '
                 'проверяем наличие обязательных полей')
    def check_objs_response(self):
        for obj in self.json['data']:
            assert 'id' in obj, \
                f"Object missing 'id' field: {obj}"
            assert 'name' in obj, \
                f"Object missing 'name' field: {obj}"
            assert 'data' in obj, \
                f"Object missing 'data' field: {obj}"

    @allure.step('Вызов get запроса и передача в него фикстуры с id')
    def challenge_one_obj(self, new_obj):
        self.response = requests.get(f'{self.url}/{new_obj}')
        self.json = self.response.json()
        return self.response

    @allure.step('Проверяем, что "id" есть в ответе')
    def checkget_id_in_response(self):
        assert "id" in self.json, \
            f"Response missing 'id' field: {self.json}"

    @allure.step('Сравниваем id в запросе с id в new_obj')
    def check_id_in_new_obj(self, new_obj):
        assert self.json['id'] == new_obj, \
            f"Expected id={new_obj}, but got {self.json['id']}"
