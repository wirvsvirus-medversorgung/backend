__author__='Max'
__status__='DEV'
class Student:
    id=None
    vorname=None
    name=None
    mail=None
    tel=None
    pw=None
    location={'long':52.375893,'lat':9.732010}
    #radius=10; #ToDo?

    def __init__(self,vorname,name,mail,tel,coord,semester,pw):
        #print(self.location)
        #print('coord:'+str(coord))
        self.id=99
        self.vorname=vorname
        self.name=name
        self.mail=mail
        self.tel=tel
        self.coordinates = coord,
        self.pw=pw
        self.semester=semester
        self.location['lat']=coord['lat']
        self.location['long']=coord['long'] #ToDo: Quickfix, stupid code
    def persist(self, db):
        #print(self.coordinates)
        lat = float(self.location['lat'])
        long = float(self.location['long'])
        self.id=db.insert_student(

           firstName=self.vorname, lastName=self.name, email=self.mail, phonenumber=self.tel,
            password=self.pw, long=long, lat=lat, semester=self.semester)

        #insert_student(self,vorname,name,mail,tel,pw,long,lat)
        #self,vorname,name,mail,tel,pw,long,lat)
        #db.insert_student(self.vorname,self.name,self.mail,self.tel,self.pw,self.location['long'],self.location['lat'])
        #studenten.append(self)
        return True

class Hospital:
    def __init__(self, name, ort, strasse, plz, gesucht, coord, vorname, nachname, mail, tel, pw):
        self.kontakt = {'vorname':None,'nachname':None,'mail':None,'tel':None,'pw':None}
        self.id=99
        self.name = name
        self.ort = ort
        self.stasse = strasse
        self.plz = plz
        self.gesucht = gesucht
        #self.coordinates = coordinates
        self.kontakt['vorname'] = vorname
        self.kontakt['nachname'] = nachname
        self.kontakt['mail'] = mail
        self.kontakt['tel'] = tel
        self.kontakt['pw'] = pw
        self.description="ToDo"
        print(coord)
        self.coordinates = {'lat': coord[0], 'long': coord[1]}# 4devtest

    #class Hospital:
   # (self, hospital_name, description, lat, long, streetAddress, postalCode, city, searchedPerson,
   #  firstName, lastName, email, phonenumber, password)

    #hospital_name, description, lat, long, streetAddress, postalCode, city,searchedPerson,
                   #     firstName, lastName, email, phonenumber, password

    def persist(self,db):
            #ToDO: DB insert
            hospitals.append(self)
            self.id=db.insert_hospital(hospital_name=self.name,description=self.description,
                               lat=self.coordinates['lat'],long=self.coordinates['lat'],
                               streetAddress=self.stasse,postalCode=self.plz,city=self.ort,searchedPerson=self.gesucht,
                               firstName=self.kontakt['vorname'],lastName=self.kontakt['nachname'],
                               email=self.kontakt['mail'],phonenumber=self.kontakt['tel'],password=self.kontakt['pw'])
            return True
    #ToDo



#studenten=[]
hospitals=[]

'''
def get_student_by_name(nachname):
    #ToDO: DB
    for s in studenten:
        if s.name == nachname:
            return s
    return "Nicht vorhnanden"
'''

def student_id_exitsts(sid):
    # ToDO: DB
    '''for s in studenten:
        print('s.id = ' + str(s.id))
        print('id = ' + str(sid))
        print(((int(s.id)) == ((int(sid)))))
        if ((int(s.id)) == ((int(sid)))):
            return True
    '''
    return False


def get_student_by_id(sid):
    # ToDO: DB
    '''
    for s in studenten:

        if int(s.id) == int(sid):
            return s
    '''

    return "Nicht vorhnanden"


def get_hospital_by_name(name):
    #ToDO: DB
    for h in hospitals:
        if h.name == name:
            return h.__dict__
    return "Nicht vorhnanden"






def find_hospitals(student,locator):
    result=locator.get_hospitals_by_coordinates(student.location['lat'],student.location['long'],student.radius)
    print(result)
    '''
            1)      Alle Kliniken die im Radius liegen

            2)

                final_result=[]
                for each r in result:
                    if get_hospital_by_name(r.name) == "Nicht vorhanden"
                        continue
                    else:
                    final_result.append(r
    '''

