import sqlite3
from abc import abstractmethod, ABC


class BasicSqliiteAdapter(ABC):
    def __init__(self,
                 table_name: str,
                 db_name: str,
                 db_url: str,
                 db_username: str,
                 db_password: str,
                 adapted_class):
        self.table_name = table_name
        self.db_name = db_name
        self.db_url = db_url
        self.db_username = db_username
        self.db_password = db_password
        self._class = adapted_class

    @property
    def adapted_class(self):
        return self._class

    @property
    def adapted_class_name(self):
        return self._class.__name__

    def _get_cursor(self):
        connection = sqlite3.connect(self.db_name)
        return connection.cursor()

    def _get_db(self):
        cursor = self._get_cursor()
        return client[self.db_name]

    def _get_table(self):
        return self._db[self.table_name]

    @abstractmethod
    def list_all(self):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, item_id):
        raise NotImplementedError

    @abstractmethod
    def save(self, serialized_data):
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity_id):
        raise NotImplementedError
