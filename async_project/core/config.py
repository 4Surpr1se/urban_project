from utils.lru_cache import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"


class ProjectConfig(BaseConfig):
    project_name: str = Field('movies', description='Имя проекта', alias='PROJECT_NAME')

    def __hash__(self):
        return hash(self.project_name)


class SqliteConfig(BaseConfig):
    filename: str = Field('sb.sqlite3', description='Файлнейм sqlite', alias='SQLITE_FILENAME')


@lru_cache()
def get_project_config() -> ProjectConfig:
    return ProjectConfig()


@lru_cache()
def get_sqlite_config() -> SqliteConfig:
    return SqliteConfig()
