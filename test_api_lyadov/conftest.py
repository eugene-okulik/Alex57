import pytest
import requests
from endpoints.create_post import CreatePost
from endpoints.create_get import CreateGet
from endpoints.update_put import UpdatePut
from endpoints.update_patch import UpdatePatch
from endpoints.update_delete import UpdateDelete


@pytest.fixture()
def create_new_obj():
    return CreatePost()


@pytest.fixture()
def get_all_obj():
    return CreateGet()


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
    print(response)
    return response['id']


@pytest.fixture()
def put_obj():
    return UpdatePut()


@pytest.fixture()
def patch_obj():
    return UpdatePatch()


@pytest.fixture()
def delete_obj():
    return UpdateDelete()

