import requests
import time


def test_api_all_obj():
    for i in range(20):
        start_time = time.time()
        response = requests.get('http://167.172.172.115:52353/object').json()
        end_time = time.time()
        request_time = end_time - start_time

        print(f"Запрос #{i + 1}: {request_time:.3f} секунд")
        print(response)
