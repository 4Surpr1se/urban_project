from fastapi import Depends

from async_project.orm.user_orm import get_user_orm
from async_project.services.base_service import BaseService
from async_project.utils.lru_cache import lru_cache


class UserService(BaseService):
    def __init__(self, user_orm: Depends(get_user_orm)):
        self.orm = user_orm


@lru_cache(capacity=1)
def get_user_service():
    return UserService()
