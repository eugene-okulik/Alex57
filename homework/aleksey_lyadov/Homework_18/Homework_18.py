import requests
import allure


def all_obj():
    response = requests.get(
        'http://167.172.172.115:52353/object').json()
    print(response)


def one_obj():
    obj_id = 544
    response = requests.get(
        f'http://167.172.172.115:52353/object/{obj_id}').json()
    print(response)


def post_obj():
    body = {"name": "homework18_test",
            "data": {
                "color": "test_homework18_color2",
                "size": "test_homework18_size2"
            }
            }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=body).json()
    print(response)


def new_obj():
    body = {"name": "homework18_test",
            "data": {
                "color": "test_homework18_color2",
                "size": "test_homework18_size2"
            }
            }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=body).json()
    return response['id']


def put_obj():
    id_obj = new_obj()
    body = {"name": "homework1812313",
            "data": {
                "color": "113131homework18_color2",
                "size": "1313133homework18_size2"
            }
            }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{id_obj}', json=body)
    print(response.json())


def patch_obj():
    id_obj = new_obj()
    body = {"name": "homework1812313",
            "data": {
                "color": "113131homework18_color2",
                "size": "1313133homework18_size2"
            }
            }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{id_obj}', json=body)
    print(response.json())


def delete_obj():
    id_obj = new_obj()
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{id_obj}')
    print(response.status_code)


all_obj()
one_obj()
post_obj()
put_obj()
patch_obj()
delete_obj()
