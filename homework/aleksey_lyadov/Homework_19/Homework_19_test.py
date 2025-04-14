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
    # Проверяем, что ответ содержит поле 'data' и это список
    assert 'data' in response, \
        "Response doesn't contain 'data' field"
    assert isinstance(response['data'], list), \
        "'data' is not a list"
    # Для каждого объекта в data проверяем наличие обязательных полей
    for obj in response['data']:
        assert 'id' in obj, \
            f"Object missing 'id' field: {obj}"
        assert 'name' in obj, \
            f"Object missing 'name' field: {obj}"
        assert 'data' in obj, \
            f"Object missing 'data' field: {obj}"
    print(response)


@pytest.fixture()
def new_obj():
    body = {"name": "homework18_test222222222",
            "data": {
                "color": "test_homework18_color33333333333",
                "size": "test_homework18_size444444444"
            }
            }
    response = requests.post(
        'http://167.172.172.115:52353/object', json=body).json()
    assert response['name'] == body['name'], \
        f"Expected name {body['name']}, but got {response['name']}"
    assert response['data']['color'] == body['data']['color'], \
        (f"Expected color {body['data']['color']}, "
         f"but got {response['data']['color']}")
    assert response['data']['size'] == body['data']['size'], \
        (f"Expected size {body['data']['size']}, "
         f"but got {response['data']['size']}")
    print(response)
    return response['id']


def test_one_obj(new_obj):
    response = requests.get(
        f'http://167.172.172.115:52353/object/{new_obj}').json()
    # Проверяем, что 'id' есть в ответе и он равен obj_id
    assert 'id' in response, \
        f"Response missing 'id' field: {response}"
    assert response['id'] == new_obj, \
        f"Expected id={new_obj}, but got {response['id']}"
    print(response)


@pytest.mark.critical
@pytest.mark.parametrize("name, color, size", [
    ("homework18_test11", "test_homework18_color11", "test_homework18_size11"),
    ("homework18_test22", "test_homework18_color22", "test_homework18_size22"),
    ("homework18_test33", "test_homework18_color33", "test_homework18_size33")
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
        f'http://167.172.172.115:52353/object/{new_obj}', json=body).json()
    assert response['name'] == body['name'], \
        f"Expected name {body['name']}, but got {response['name']}"
    assert response['data']['color'] == body['data']['color'], \
        (f"Expected color {body['data']['color']}, "
         f"but got {response['data']['color']}")
    assert response['data']['size'] == body['data']['size'], \
        (f"Expected size {body['data']['size']}, "
         f"but got {response['data']['size']}")
    print(response)


def test_patch_obj(new_obj):
    body = {"name": "homework181231311111",
            "data": {
                "color": "113131homework18_color11112",
                "size": "1313133homework18_size11112"
            }
            }
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{new_obj}', json=body).json()
    assert response['name'] == body['name'], \
        f"Expected name {body['name']}, but got {response['name']}"
    assert response['data']['color'] == body['data']['color'], \
        (f"Expected color {body['data']['color']}, "
         f"but got {response['data']['color']}")
    assert response['data']['size'] == body['data']['size'], \
        (f"Expected size {body['data']['size']}, "
         f"but got {response['data']['size']}")
    print(response)


def test_delete_obj(new_obj):
    response = requests.delete(
        f'http://167.172.172.115:52353/object/{new_obj}')
    assert response.status_code == 200, \
        f"Failed status code {response.status_code}"
    print(response.status_code)
