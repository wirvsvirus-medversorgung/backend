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
        self.__connection = sqlite3.connect(self.file)

    def disconnect(self):
        if self.__connection:
            self.__connection.close()
            self.__connection = None

    def init_db(self):
        self.__connection.execute('''CREATE TABLE Hospital
        (id         INT     PRIMARY KEY             ,
        name        TEXT                    NOT NULL,
        description TEXT                    NOT NULL,
        lat         REAL                    NOT NULL,
        long        REAL                    NOT NULL,
        streetAddress   TEXT                NOT NULL,
        postalCode  TEXT                    NOT NULL,
        city        TEXT                    NOT NULL,
        contactPersonId INT                 NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE Person
        (id         INT     PRIMARY KEY             ,
        firstName   TEXT                    NOT NULL,
        lastName    TEXT                    NOT NULL,
        email       TEXT                    NOT NULL,
        phoneNumber TEXT                            ,
        password    TEXT                    NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE Student
        (id         INT     PRIMARY KEY             ,
        personId    INT                     NOT NULL,
        lat         REAL                    NOT NULL,
        long        REAL                    NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE SearchedPerson
        (id         INT     PRIMARY KEY             ,
        hospitalId  INT                     NOT NULL,
        fieldOfApplicationId INT            NOT NULL,
        priorMedicalExperienceId    INT     NOT NULL,
        competenciesId  INT                 NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE SP_FoA
        (id         INT     PRIMARY KEY             ,
        searchedPersonID   INT              NOT NULL,
        fieldOfApplicationID    INT         NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE FieldOfApplication
        (id         INT     PRIMARY KEY             ,
        applicationField    TEXT            NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE SP_PME
        (id         INT     PRIMARY KEY             ,
        searchedPersonID   INT              NOT NULL,
        priorMedicalExperienceID    INT     NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE PriorMedicalExperience
        (id         INT     PRIMARY KEY             ,
        experience  TEXT                    NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE SP_C
        (id         INT     PRIMARY KEY             ,
        searchedPersonID   INT              NOT NULL,
        competenciesID    INT               NOT NULL
        );
        ''')

        self.__connection.execute('''CREATE TABLE Competencies
        (id         INT     PRIMARY KEY             ,
        competencies  TEXT                   NOT NULL
        );
        ''')

        self.insert_field_of_application()
        self.insert_prior_medical_experience()
        self.insert_competencies()

    def insert_field_of_application(self):
        fields = ['innere Medizin', 'Chirurgie', 'Anästhesie/Intensivmedizin', 'Notfallaufnahme', 'Radiologie',
                  'Telefonberatung']
        for x in range(len(fields)):
            values = (x + 1, fields[x])
            statement = "INSERT INTO FieldOfApplication(ID, applicationField) VALUES (?,?)"
            cur = self.__connection.cursor()
            cur.execute(statement, values)
            self.__connection.commit()
            cur.close()

    def insert_prior_medical_experience(self):
        fields = ['Abgeschlossene pflegerische Ausbildung', 'Intensivpflege', 'Beatmungserfahrung',
                  'Operationstechnische Assistenz', 'Hakenhalter/-in', 'Medizinisch-technische Assistenz',
                  'Notfallsanitäter/-in', 'Rettungssanitäter/-in', 'Laborerfahrung']
        for x in range(len(fields)):
            values = (x + 1, fields[x])
            statement = "INSERT INTO PriorMedicalExperience(ID, experience) VALUES (?,?)"
            cur = self.__connection.cursor()
            cur.execute(statement, values)
            self.__connection.commit()
            cur.close()

    def insert_competencies(self):
        fields = ['Blutentnahme', 'Periphere Venenzugänge', 'Medikamente und Infusionen richten', 'Impfen']
        for x in range(len(fields)):
            values = (x + 1, fields[x])
            statement = "INSERT INTO Competencies(ID, competencies) VALUES (?,?)"
            cur = self.__connection.cursor()
            cur.execute(statement, values)
            self.__connection.commit()
            cur.close()

    def insert_hospital(self, hospital_name, hospital_description, lat, long, streetAddress, postalCode, city,
                        firstName, lastName, email, phonenumber, password):

        b = password.encode('utf-8')
        statement = 'INSERT INTO Person(id,firstName,lastName, email, phoneNumber, password) VALUES (NULL,?,?,?,?,?);'
        values = (firstName, lastName, email, phonenumber, bcrypt.hashpw(b, self.salt))
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        personid = cur.lastrowid
        cur.close()
        statement = 'INSERT INTO Hospital(id,name, description, lat, long, streetAddress, postalCode, city, contactPersonId) VALUES(NULL,?,?,?,?,?,?,?,?)'
        values = (hospital_name, hospital_description, lat, long, streetAddress, postalCode, city, personid)
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        cur.close()

    def insert_student(self, firstName, lastName, email, phonenumber, password, long, lat):
        b = password.encode('utf-8')
        statement = 'INSERT INTO Person(id,firstName,lastName, email, phoneNumber, password) VALUES (NULL,?,?,?,?,?);'
        values = (firstName, lastName, email, phonenumber, bcrypt.hashpw(b, self.salt))
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        personid = cur.lastrowid
        cur.close()
        statement = 'INSERT INTO Student(id, personId, lat, long) VALUES(NULL,?,?,?)'
        values = (personid, lat, long)
        cur = self.__connection.cursor()
        cur.execute(statement, values)
        self.__connection.commit()
        cur.close()