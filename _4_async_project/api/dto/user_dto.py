from pydantic import BaseModel

from async_project.models.user import User


class UserDto(BaseModel):
    id: str
    name: str

    @classmethod
    def from_model(cls, model: User):
        return cls(id=model.id, name=model.name)


class UserCreateDto(UserDto):
    pass
