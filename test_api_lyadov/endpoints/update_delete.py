import requests
import allure
from endpoints.endpoint import Endpoint


class UpdateDelete(Endpoint):

    @allure.step('Обновление delete запросом')
    def update_obj_delete(self, new_obj):
        self.response = requests.delete(f'{self.url}/{new_obj}')
        # self.json = self.response.json()
        return self.response
