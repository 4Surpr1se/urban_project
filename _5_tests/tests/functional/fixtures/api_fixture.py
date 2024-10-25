from http import HTTPStatus

import aiohttp
import pytest_asyncio

from tests.functional.settings import test_settings


@pytest_asyncio.fixture(name='api_session')
async def api_session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture(name='make_get_request')
async def make_get_request(api_session):
    async def inner(url: str, params: dict = None, headers: dict = None):
        full_url = test_settings.service_url + url
        async with api_session.get(full_url, params=params, headers=headers) as response:
            body = await response.json()
            return response, body

    return inner


@pytest_asyncio.fixture(name='make_post_request')
def make_post_request(api_session):
    async def inner(url: str, data: dict = None, headers: dict = None):
        full_url = test_settings.service_url + url
        async with api_session.post(full_url, json=data, headers=headers) as response:
            body = await response.json()
            return response, body

    return inner


@pytest_asyncio.fixture(name='make_put_request')
async def make_put_request(api_session):
    async def inner(url: str, data: dict = None, headers: dict = None):
        full_url = test_settings.service_url + url
        async with api_session.put(full_url, json=data, headers=headers) as response:
            body = await response.json()
            return response, body

    return inner


@pytest_asyncio.fixture(name='make_delete_request')
async def make_delete_request(api_session):
    async def inner(url: str, data: dict = None, headers: dict = None):
        full_url = test_settings.service_url + url
        async with api_session.delete(full_url, json=data, headers=headers) as response:
            body = await response.json()
            return response, body

    return inner
