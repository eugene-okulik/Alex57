import requests
import allure
from endpoints.endpoint import Endpoint


class UpdatePatch(Endpoint):

    @allure.step('Создаем переменную body')
    def create_body_patch(self):
        body = {"name": "homework1812313",
                "data": {
                    "color": "113131homework18_color2",
                    "size": "1313133homework18_size2"
                }
                }
        return body

    @allure.step('Обновление patch запросом')
    def update_obj_patch(self, new_obj, body):
        self.response = requests.patch(f'{self.url}/{new_obj}', json=body)
        self.json = self.response.json()
        return self.response
