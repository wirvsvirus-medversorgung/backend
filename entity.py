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
    radius=10;

    def __init__(self,vorname,name,mail,tel):
        self.id=99
        self.vorname=vorname
        self.name=name
        self.mail=mail
        self.tel=tel

        self.pw='TEST23'


    def persist(self, db):
        #ToDO: DB insert
        #insert_student(self,vorname,name,mail,tel,pw,long,lat)
        #self,vorname,name,mail,tel,pw,long,lat)
        #db.insert_student(self.vorname,self.name,self.mail,self.tel,self.pw,self.location['long'],self.location['lat'])
        studenten.append(self)
        return True


class Hospital:
    id=None
    benoetigt = {'pfleger': 0, 'ota': 0}  # differnzierung nach berufsgruppen?
    name=None
    ort=None
    stasse=None
    hausnr=None
    plz=None
    covid_patienten=None
    coordinates = {'long': -1, 'lat': -2}
    """"
         @ Map-Team
   
   ToDo:  coordinates = klinik_locator.get_coordinates_by_name(name)
    
    Anmerkung: name stammt aus der Liste, ein Name zu dem es keine Coordinaten gibt kann nicht kommen
    
    ToDO: hospitals=klinik_locator.get_hospitals_by_coordinates(origin, radius)
    
    Anmerkung: Oring und Radius kommen vom UI
    
    """



    def __init__(self,name,ort,strasse,hausnr,plz,coordinates):
        self.name=name
        self.ort=ort
        self.stasse=strasse
        self.hausnr=hausnr
        self.plz=plz
        #self.covid_patienten=covid_patienten
        self.coordinates=coordinates


    def persist(self):
        #ToDO: DB insert
        hospitals.append(self)
        return True
    #ToDo



studenten=[]

hospitals=[]

def get_student_by_name(nachname):
    #ToDO: DB
    for s in studenten:
        if s.name == nachname:
            return s
    return "Nicht vorhnanden"


def student_id_exitsts(sid):
    # ToDO: DB
    for s in studenten:
        print('s.id = ' + str(s.id))
        print('id = ' + str(sid))
        print(((int(s.id)) == ((int(sid)))))
        if ((int(s.id)) == ((int(sid)))):
            return True
    return False


def get_student_by_id(sid):
    # ToDO: DB
    for s in studenten:

        if int(s.id) == int(sid):
            return s


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

