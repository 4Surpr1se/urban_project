from http import HTTPStatus

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from dto.user_dto import UserDto, UserCreateDto
from models.pagination_params import PaginateQueryParams
from services.user_service import UserService, get_user_service

router = APIRouter()


@router.get(
    "/",
    response_model=List[UserDto],
    summary="Получение списка Пользователей",
    description="Позволяет получить список всех пользователей",
)
async def get_users(pagination: Annotated[PaginateQueryParams, Depends()],
                    service: UserService = Depends(get_user_service)):
    users = await service.get_all(pagination.page_number, pagination.page_size)
    return [
        UserDto.from_model(user) for user in users
    ]


@router.post(
    "/",
    response_model=UserDto,
    summary="Создание пользователя",
    description="Позволяет создать пользователя",
)
async def create_user(user_data: UserCreateDto, service: UserService = Depends(get_user_service)):
    if user := await service.create(user_data):
        return UserDto.from_model(user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user not found')


@router.get(
    "/{user_id}",
    response_model=UserDto,
    summary="Получение пользователя по ID",
    description="Позволяет получить пользователя по его ID",
)
async def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    if user := await service.get_by_id(user_id):
        return UserDto.from_model(user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user not found')


@router.put(
    "/{user_id}",
    response_model=UserDto,
    summary="Обновление пользователя по ID",
    description="Позволяет обновлять пользователя по его ID",
)
async def update_user(user_id: int, service: UserService = Depends(get_user_service)):
    if user := await service.update(user_id):
        return UserDto.from_model(user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user not found')


@router.delete(
    "/{user_id}",
    response_model=UserDto,
    summary="Удаление пользователя по ID",
    description="Позволяет удалять пользователя по его ID",
)
async def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    if user := await service.delete(user_id):
        return UserDto.from_model(user)

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user not found')
