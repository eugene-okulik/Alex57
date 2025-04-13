import requests
import pytest


@pytest.fixture(scope='session')
def text_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def text_before():
    print('before test')
    yield
    print('after test')


def test_all_obj(text_testing):
    response = requests.get(
        'http://167.172.172.115:52353/object').json()
    print(response)


def test_one_obj():
    obj_id = 5004
    response = requests.get(
        f'http://167.172.172.115:52353/object/{obj_id}').json()
    print(response)


@pytest.mark.critical
def test_post_obj():
    body = {"name": "homework18_test",
            "data": {
                "color": "test_homework18_color2",
                "size": "test_homework18_size2"
            }
            }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=body).json()
    print(response)


@pytest.fixture()
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


@pytest.mark.parametrize("name, color, size", [
    ("homework18_test1", "test_homework18_color1", "test_homework18_size1"),
    ("homework18_test2", "test_homework18_color2", "test_homework18_size2"),
    ("homework18_test3", "test_homework18_color3", "test_homework18_size3")
])
def test_new_obj(name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=body).json()
    assert "id" in response
    print(response["id"])


@pytest.mark.medium
def test_put_obj(new_obj):
    body = {"name": "homework1812313",
            "data": {
                "color": "113131homework18_color2",
                "size": "1313133homework18_size2"
            }
            }
    response = requests.put(
        f'http://167.172.172.115:52353/object/{new_obj}', json=body)
    print(response.json())


def test_patch_obj(new_obj):
    body = {"name": "homework1812313",
            "data": {
                "color": "113131homework18_color2",
                "size": "1313133homework18_size2"
            }
            }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_obj}', json=body)
    print(response.json())


def test_delete_obj(new_obj):
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{new_obj}')
    print(response.status_code)
