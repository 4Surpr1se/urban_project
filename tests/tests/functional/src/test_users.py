import pytest
from http import HTTPStatus

pytestmark = pytest.mark.asyncio


async def test_create_user(make_post_request, user_data):
    response, body = await make_post_request("/", user_data)
    assert response.status == HTTPStatus.OK
    assert user_data == body


async def test_get_user(make_post_request, make_get_request, user_data):
    await make_post_request("/", user_data)
    response, body = await make_get_request(f"/{user_data['id']}", user_data)
    assert response.status == HTTPStatus.OK
    assert user_data == body


async def test_get_users(make_post_request, make_get_request, user_data, user_data_second):
    await make_post_request("/", user_data)
    await make_post_request("/", user_data_second)
    response, body = await make_get_request("/", user_data)
    assert response.status == HTTPStatus.OK
    assert [user_data, user_data_second] == body


async def test_update_users(make_post_request, make_get_request, make_put_request, user_data, user_data_second):
    await make_post_request("/", user_data)
    edited_user = dict(user_data, **{'name': user_data_second['name']})
    await make_put_request(f"/{user_data['id']}", edited_user)
    response, body = await make_get_request(f"/{user_data['id']}")
    assert response.status == HTTPStatus.OK
    assert edited_user == body


async def test_delete_users(make_post_request, make_get_request, make_delete_request, user_data):
    await make_post_request("/", user_data)
    await make_delete_request(f"/{user_data['id']}")
    response, body = await make_get_request(f"/{user_data['id']}")
    assert response.status == HTTPStatus.NOT_FOUND
