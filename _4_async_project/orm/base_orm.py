from sqlite3 import Connection

from pydantic import BaseModel

from async_project.utils.lru_cache import lru_cache

# https://pypi.org/project/pydantic_sqlite/
class BaseOrm:
    model: BaseModel
    table_name: str

    @lru_cache
    def __init__(self, connection: Connection):
        self.connection = connection

    def _get_cursor(self):
        return self.connection.cursor()

    @staticmethod
    def _execute_query(cursor, query, params=None):
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

    def get_all(self, *field_names):
        cursor = self._get_cursor()
        self._execute_query(cursor,
                            f'SELECT {", ".join(field_names) or "*"} FROM {self.table_name}')
        return cursor.fetchall()

    def create(self, values):
        cursor = self._get_cursor()
        self._execute_query(cursor,
                            f'INSERT INTO {self.table_name} ({", ".join(self.fields)}) VALUES ({("?," * len(self.fields))[:-1]});',
                            values)
        self.connection.commit()

    def update_by_id(self, id, new_data):
        cursor = self._get_cursor()
        set_clause = ', '.join([f"{k} = ?" for k in new_data.keys()])
        values = tuple(new_data.values()) + (id,)
        query = f'UPDATE {self.table_name} SET {set_clause} WHERE id = ?'

        self._execute_query(cursor, query, values)
        self.connection.commit()

    def delete_by_id(self, id):
        cursor = self._get_cursor()
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self._execute_query(cursor, query, (id,))
        self.connection.commit()
