from typing import Optional

from sqlite3 import Connection

sqlite_connection: Optional[Connection] = None


# Функция понадобится при внедрении зависимостей
async def get_sqlite() -> Optional[Connection]:
    return sqlite_connection
