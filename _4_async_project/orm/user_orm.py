from async_project.db.sqlite import get_sqlite
from async_project.models.user import User
from async_project.orm.base_orm import BaseOrm
from fastapi import Depends

from async_project.utils.lru_cache import lru_cache


class UserOrm(BaseOrm):
    model = User
    table_name = 'user'


@lru_cache
def get_user_orm(sql_conn: Depends(get_sqlite)):
    return UserOrm(sql_conn)
