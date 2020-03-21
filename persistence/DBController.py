from .SQLite3Manager import SQLite3Manager
__author__='Marc'
__status__='DEV'


class DBController:

    __dbtype = None
    __validTypes = "sqlite3", "mysql"
    __connection = None

    def __init__(self, dbtype):
        if dbtype in self.__validTypes:
            self.__dbtype = dbtype

    def __connect(self):
        if self.__dbtype == "sqlite3":
            self.__connection = SQLite3Manager("/path/to/sqlite3")
            self.__connection.connect()

    def insert(self, word):
        if not self.__connection:
            self.__connect()

    def test_db(self):
        self.__connect()
        self.__connection.init_db()
        self.__connection.insert_hospital(1, "Hospital", "city1", "street1", 1, 12345, 12)
