import sqlite3
import bcrypt

__author__ = 'Marc, Hendrik'
__status__ = 'DEV'


class SQLite3Manager:
    file = None
    __connection = None
    salt = None

    def __init__(self, file):
        self.file = file
        self.salt = bcrypt.gensalt()

    def __del__(self):
        if self.__connection:
            self.__connection.close()

    def connect(self):
        if not self.file:
            self.file = ":memory:"
        self.__connection = sqlite3.connect(self.file, check_same_thread=False)

    def disconnect(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def init_db(self):
        self.__connection.execute('''CREATE TABLE Hospital
        (id         INTEGER     PRIMARY KEY         ,
        name        TEXT                    NOT NULL,
        description TEXT                    NOT NULL,
        lat         REAL                    NOT NULL,
        long        REAL                    NOT NULL,
        streetAddress   TEXT                NOT NULL,
        postalCode  TEXT                    NOT NULL,
        city        TEXT                    NOT NULL,
        employmentContract  INT                     ,
        searchedPerson  INT                 NOT NUll,
        contactPersonId INT                 NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE Person
        (id         INTEGER     PRIMARY KEY         ,
        firstName   TEXT                    NOT NULL,
        lastName    TEXT                    NOT NULL,
        email       TEXT                    NOT NULL,
        phoneNumber TEXT                            ,
        password    TEXT                    NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE Student
        (id         INTEGER     PRIMARY KEY         ,
        personId    INT                     NOT NULL,
        semester    INT                             ,
        lat         REAL                    NOT NULL,
        long        REAL                    NOT NULL
        );
        ''')


    def insert_hospital(self, hospital_name, description, lat, long, streetAddress, postalCode, city,searchedPerson,
                        firstName, lastName, email, phonenumber, password):
        b = password.encode('utf-8')
        statement = 'INSERT INTO Person(firstName,lastName, email, phoneNumber, password) VALUES (?,?,?,?,?);'
        values = (firstName, lastName, email, phonenumber, bcrypt.hashpw(b, self.salt))
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        personid = cur.lastrowid
        cur.close()
        statement = 'INSERT INTO Hospital(name, description, lat, long, streetAddress, postalCode, city,searchedPerson, contactPersonId) VALUES(?,?,?,?,?,?,?,?,?)'
        values = (hospital_name, description, lat, long, streetAddress, postalCode, city,(int(searchedPerson)), personid)
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        cur.close()
        return personid

    def insert_student(self, firstName, lastName, email, phonenumber, password, long, lat, semester=0):
        b = password.encode('utf-8')
        statement = 'INSERT INTO Person(firstName,lastName, email, phoneNumber, password) VALUES (?,?,?,?,?);'
        values = (firstName, lastName, email, phonenumber, bcrypt.hashpw(b, self.salt))
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        personid = cur.lastrowid
        cur.close()
        statement = 'INSERT INTO Student(personId, lat, long, semester) VALUES(?,?,?,?)'
        values = (personid, lat, long, semester)
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        cur.close()

        return personid

    def get_student(self, myid):
        cur = self.__connection.cursor()
        cur.execute("SELECT * FROM Student INNER JOIN Person ON Student.personId=Person.id WHERE Student.id=?",
                    str(myid))
        row = cur.fetchone()
        cur.close()
        return row

    def get_student_by_mail(self, email):
        cur = self.__connection.cursor()
        cur.execute("SELECT * FROM Student INNER JOIN Person ON Student.personId=Person.id WHERE Person.email=?",
                    str(email))
        row = cur.fetchone()
        cur.close()
        return row

    def get_hospital_by_id(self, myid):
        cur = self.__connection.cursor()
        cur.execute(
            "SELECT * FROM Hospital INNER JOIN Person ON Hospital.contactPersonId=Person.id WHERE Hospital.id=?",
            str(myid))
        row = cur.fetchone()
        cur.close()
        return row

    def get_hospital_by_name(self, name):
        cur = self.__connection.cursor()
        cur.execute(
            "SELECT * FROM Hospital INNER JOIN Person ON Hospital.contactPersonId=Person.id WHERE Hospital.name like ?",
            (str("%" + name + "%"),))
        row = cur.fetchone()
        cur.close()
        return row

    def student_password_correct(self,email,password):
        cur = self.__connection.cursor()
        cur.execute("SELECT Person.password FROM Student INNER JOIN Person ON Student.personId=Person.id WHERE Person.email=? " , (email,))
        dbpassword = cur.fetchone()
        cur.close()
        return bcrypt.checkpw(password.encode('utf8'), dbpassword[0])

    #def student_exists_by_id(self,sid):
