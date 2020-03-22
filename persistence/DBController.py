from .SQLite3Manager import SQLite3Manager

__author__ = 'Marc'
__status__ = 'DEV'


class DBController:
    __dbtype = None
    __validTypes = "sqlite3", "mysql"
    __connection = None

    def __init__(self, dbtype):
        if dbtype in self.__validTypes:
            self.__dbtype = dbtype
        self.__connect()

    def __connect(self):
        if self.__dbtype == "sqlite3":
            self.__connection = SQLite3Manager("sqlite3")
        self.__connection.connect()

    def insert(self, word):
        if not self.__connection:
            self.__connect()

    def insert_student(self, firstName, lastName, email, phonenumber, password, long, lat, semester=0):
        return self.__connection.insert_student(firstName, lastName, email, phonenumber, password, long, lat, semester)


    def test_db(self):
        self.__connect()
        self.__connection.init_db()
        self.__connection.insert_hospital("hosputal_name", "hospital_description", 43.6, 45.7, "Adresse", "4525",
                                          "Hannover", 25, "first", "last", "ssdas@sdas.de", "sadsa", "passw")
        self.__connection.insert_student("first", "last", "ssdas@sdas.de", "sadsa", "passw", 43.6, 45.7,5)
