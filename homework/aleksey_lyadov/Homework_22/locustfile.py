from locust import task, HttpUser


class ApiObj(HttpUser):
    new_obj = None

    def on_start(self):
        body = {"name": "homework18_test222222222",
                "data": {
                    "color": "test_homework18_color33333333333",
                    "size": "test_homework18_size444444444"
                }
                }
        response = self.client.post('/object', json=body)
        self.new_obj = response.json()['id']

    @task(5)
    def get_one_obj(self):
        self.client.get(f'/object/{self.new_obj}')

    @task(1)
    def put_obj(self):
        body = {"name": "homework1812313",
                "data": {
                    "color": "113131homework18_color2",
                    "size": "1313133homework18_size2"
                }
                }
        self.client.put(f'/object/{self.new_obj}', json=body)

    @task(2)
    def patch_obj(self):
        body = {"name": "homework181231311111",
                "data": {
                    "color": "113131homework18_color11112",
                    "size": "1313133homework18_size11112"
                }
                }
        self.client.patch(f'/object/{self.new_obj}', json=body)

    def on_stop(self):
        self.client.delete(f'/object/{self.new_obj}')
