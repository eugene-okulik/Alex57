import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePut(Endpoint):

    @allure.step('Создаем переменную body')
    def create_body_put(self):
        body = {"name": "homework1812313",
                "data": {
                    "color": "113131homework18_color2",
                    "size": "1313133homework18_size2"
                }
                }
        return body

    @allure.step('Обновление put запросом')
    def update_obj_put(self, new_obj, body):
        self.response = requests.put(f'{self.url}/{new_obj}', json=body)
        self.json = self.response.json()
        return self.response
