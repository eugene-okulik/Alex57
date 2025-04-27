import requests
import allure
from endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    TEST_DATA = [
        ("homework18_test11",
         "test_homework18_color11", "test_homework18_size11"),
        ("homework18_test22",
         "test_homework18_color22", "test_homework18_size22"),
        ("homework18_test33",
         "test_homework18_color33", "test_homework18_size33")
    ]

    @allure.step('Создаем переменную body '
                 'и передаем в нее параметры из parametrize')
    def create_body(self, name, color, size):
        body = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        return body

    @allure.step('Вызов post запроса с передачей '
                 'в него параметров из переменной body')
    def create_new_post(self, body):
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
        return self.response

    @allure.step('Проверяем, что "id" есть в ответе')
    def check_id_in_response(self):
        assert "id" in self.json

    @allure.step('Сравнивает ответ с ожидаемыми значениями')
    def check_body_and_response(self, name, color, size):
        assert self.json["name"] == name
        assert self.json["data"]["color"] == color
        assert self.json["data"]["size"] == size
