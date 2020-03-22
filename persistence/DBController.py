from .SQLite3Manager import SQLite3Manager

__author__ = 'Marc, Hendrik, Max'
__status__ = 'DEV'



class DBController:
    '''
        Final
    '''
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

    def test_db(self):
        self.__connect()
        self.__connection.init_db()
        self.__connection.insert_hospital("hosputal_name", "hospital_description", 43.6, 45.7, "Adresse", "4525",
                                          "Hannover", 25, "first", "last", "ssdas@sdas.de", "sadsa", "passw")
        self.__connection.insert_student("first", "last", "ssdas@sdas.de", "sadsa", "passw", 43.6, 45.7,5)

    def student_exists(self,email,password):
        auth_check=self.__connection.student_password_correct(email,password)
        return auth_check
    '''
        In Proc
    '''


    def get_student(self,sid):
        #sid = self.__connection.insert_student("first", "last", "test@gmx.de", "05121451", "passw", 43.6, 45.7, 5)
        res= self.__connection.get_student(sid)
        return res

    def get_student_location(self,sid):
        res= self.__connection.get_student_location(sid)
        return res

    def get_student_by_mail(self,mail):
        return self.__connection.get_student_by_mail(mail)

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
