from abc import ABC, abstractmethod

from async_project.orm.base_orm import BaseOrm
from pydantic import BaseModel


# TODO: Is BaseService abstract class?
class BaseService(ABC):

    @abstractmethod
    def __init__(self, orm: BaseOrm):
        self.orm = orm

    def get_all(self):
        return self.orm.get_all()

    def get_by_id(self, id: int):
        return self.orm.get_by_id(id)

    def create(self, data: BaseModel):
        return self.orm.create(data)

    def update(self, id: int, data: BaseModel):
        return self.orm.update_by_id(id, data)

    def delete(self, id: int):
        return self.orm.delete_by_id(id)
