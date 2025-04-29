import allure


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Проверка объектов в ответе и в body')
    def check_objs_in_body(self, body):
        assert self.json['name'] == body['name'], \
            f"Expected name {body['name']}, but got {self.json['name']}"
        assert self.json['data']['color'] == body['data']['color'], \
            (f"Expected color {body['data']['color']}, "
             f"but got {self.json['data']['color']}")
        assert self.json['data']['size'] == body['data']['size'], \
            (f"Expected size {body['data']['size']}, "
             f"but got {self.json['data']['size']}")
