from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from core.config import get_sqlite_config
from db import sqlite
from sqlite3 import Connection


@asynccontextmanager
async def lifespan(app: FastAPI, sqlite_config: Depends(get_sqlite_config)):
    sqlite.sqlite_connection = Connection(database=sqlite_config.filename)

    yield

    await sqlite.sqlite_connection.close()  # todo ?
