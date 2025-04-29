import pytest
import requests
from endpoints.create_post import CreatePost
from endpoints.update_put import UpdatePut
from endpoints.update_patch import UpdatePatch
from endpoints.update_delete import UpdateDelete
from endpoints.update_get import UpdateGet


@pytest.fixture()
def create_new_obj():
    return CreatePost()


@pytest.fixture()
def get_all_obj():
    return UpdateGet()


@pytest.fixture()
def new_obj():
    body = {"name": "homework18_test222222222",
            "data": {
                "color": "test_homework18_color33333333333",
                "size": "test_homework18_size444444444"
            }
            }
    response = CreatePost().generate_new_objects(body)
    response_data = response.json()
    obj_id = response_data['id']
    print(f"Created object with ID: {obj_id}")
    yield response_data['id']
    print(f"Deleting object with ID: {obj_id}")
    UpdateDelete().update_obj_delete(obj_id)


@pytest.fixture()
def put_obj():
    return UpdatePut()


@pytest.fixture()
def patch_obj():
    return UpdatePatch()


@pytest.fixture()
def delete_obj():
    return UpdateDelete()
