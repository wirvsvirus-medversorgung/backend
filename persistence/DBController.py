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

    def insert_hospital(self, hospital_name, description, lat, long, streetAddress, postalCode, city,searchedPerson,
                        firstName, lastName, email, phonenumber, password):

        return self.__connection.insert_hospital(hospital_name, description, lat, long, streetAddress, postalCode, city, searchedPerson,
                        firstName, lastName, email, phonenumber, password)


    def student_exists(self,email,password):
        row=self.__connection.student_exists(email,password)
        if row is None:
            return False
        if(len(row)==0):
            return False
        else:
            return True
    '''
        def student_exists_by_id(self,sid):
            row = self.__connection.student_exists_by_id(sid)
            if row is None:
                return False
            if (len(row) == 0):
                return False
            else:
                return True
    '''
    def test_db(self):
        self.__connect()
        self.__connection.init_db()
        self.__connection.insert_hospital("My Hospital Hannover", "hospital_description", 43.6, 45.7, "Adresse", "4525",
                                          "Hannover", 25, "first", "last", "ssdas@sdas.de", "sadsa", "passw")
        self.__connection.insert_student("first", "last", "test@gmx.de", "05121451", "passw", 43.6, 45.7,5)
        print(self.__connection.student_password_correct("test@gmx.de", "passw"))
        print(self.__connection.student_password_correct("test@gmx.de", "passwsd"))
        print(self.__connection.get_hospital_by_id(1))
        print(self.__connection.get_hospital_by_name("Hannover"))