import sqlite3
__author__='Marc'
__status__='DEV'


class SQLite3Manager:
    file = None
    __connection = None

    def __init__(self, file):
        self.file = file

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    def connect(self):
        if not self.file:
            self.file = ":memory:"
        self.__connection = sqlite3.connect(self.file)

    def disconnect(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def init_db(self):
        self.__connection.execute('''CREATE TABLE HOSPITAL
        (ID         INT     PRIMARY KEY     NOT NULL,
        NAME        TEXT                    NOT NULL,
        LOCATION    TEXT                    NOT NULL,
        STREET      TEXT                    NOT NULL,
        NO          INT                     NOT NULL,
        ZIP         INT                     NOT NULL,
        COVID       INT                     NOT NULL);
        ''')

    def insert_hospital(self, hospital_id, hospital_name, hospital_location, hospital_street, hospital_no, hospital_zip, hospital_covid):
        statement = "INSERT INTO HOSPITAL (ID,NAME,LOCATION,STREET,NO,ZIP,COVID) VALUES ({},'{}','{}','{}',{},{},{})"
        statement = statement.format(hospital_id, hospital_name, hospital_location, hospital_street,
                                     hospital_no, hospital_zip, hospital_covid)
        self.__connection.execute(statement)

        self.__connection.commit()
