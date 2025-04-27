import pytest
import allure
from endpoints.create_post import CreatePost


@allure.feature('Manipulate post')
@allure.story('Post')
@allure.title('Создание 3 новых объекта')
@pytest.mark.critical
@pytest.mark.parametrize("name, color, size", CreatePost().TEST_DATA)
def test_new_obj(name, color, size, create_new_obj):
    create_new_obj.create_new_post(
        create_new_obj.create_body(name, color, size))
    create_new_obj.check_status_is_200()
    create_new_obj.check_id_in_response()
    create_new_obj.check_body_and_response(name, color, size)


@allure.feature('Get post')
@allure.story('Get')
@allure.title('Получение всех объектов')
def test_all_obj(get_all_obj):
    get_all_obj.challenge_all_obj()
    get_all_obj.check_status_is_200()
    get_all_obj.check_data_response()
    get_all_obj.check_objs_response()


@allure.feature('Get post')
@allure.story('Get')
@allure.title('Получение одного объекта')
def test_one_obj(get_all_obj, new_obj):
    get_all_obj.challenge_one_obj(new_obj)
    get_all_obj.check_status_is_200()
    get_all_obj.checkget_id_in_response()
    get_all_obj.check_id_in_new_obj(new_obj)


@allure.feature('Manipulate post')
@allure.story('Put')
@allure.title('Обновление put запросом')
@pytest.mark.medium
def test_put_obj(put_obj, new_obj):
    body = put_obj.create_body_put()
    put_obj.update_obj_put(new_obj, body)
    put_obj.check_status_is_200()
    put_obj.check_objs_in_body(body)


@allure.feature('Manipulate post')
@allure.story('Patch')
@allure.title('Обновление patch запросом')
def test_patch_obj(patch_obj, new_obj):
    body = patch_obj.create_body_patch()
    patch_obj.update_obj_patch(new_obj, body)
    patch_obj.check_status_is_200()
    patch_obj.check_objs_in_body(body)


@allure.feature('Manipulate post')
@allure.story('Delete')
@allure.title('Удаление объекта')
def test_delete_obj(delete_obj, new_obj):
    delete_obj.update_obj_delete(new_obj)
    delete_obj.check_status_is_200()
