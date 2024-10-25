import pytest
from http import HTTPStatus

pytestmark = pytest.mark.asyncio

async def test_rate_limiting(make_get_request, make_post_request, user_data):
    # Регистрация пользователя и получение токена доступа
    response, body = await make_post_request("/api/v1/auth/register", user_data)
    token = body["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Предполагается, что лимит запросов установлен на 5 запросов в минуту для тестов
    url = "/api/v1/auth/me"
    rate_limit = 5  # Установите лимит, соответствующий настройкам в тестовой среде

    # Отправляем запросы до достижения лимита
    for _ in range(rate_limit):
        response, body = await make_get_request(url, headers=headers)
        assert response.status == HTTPStatus.OK

    # Следующий запрос должен вернуть ошибку 429
    response, body = await make_get_request(url, headers=headers)
    assert response.status == HTTPStatus.TOO_MANY_REQUESTS
    assert body == {"detail": "Too many requests. Try again later."}


async def test_x_request_id_header(make_get_request, make_post_request, user_data):
    # Регистрация пользователя и получение токена доступа
    response, body = await make_post_request("/api/v1/auth/register", user_data)
    token = body["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Тест без заголовка x-request-id
    response, body = await make_get_request("/api/v1/auth/me", headers=headers)
    assert response.status == HTTPStatus.OK
    assert "x-request-id" in response.headers
    generated_request_id = response.headers["x-request-id"]
    assert generated_request_id is not None

    # Тест с пользовательским заголовком x-request-id
    custom_request_id = "test-request-id-123"
    headers["x-request-id"] = custom_request_id
    response, body = await make_get_request("/api/v1/auth/me", headers=headers)
    assert response.status == HTTPStatus.OK
    assert "x-request-id" in response.headers
    assert response.headers["x-request-id"] == custom_request_id
