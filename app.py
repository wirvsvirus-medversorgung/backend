from flask import Flask
from flask import request
from flask import jsonify
from flask_swagger import swagger
from entity import *
import entity
from clinic_locator import ClinicLocator
from persistence.DBController import DBController
__author__='Max'
__status__='DEV'


app = Flask(__name__)
locator=ClinicLocator()
db=DBController("sqlite3")

@app.route('/')
def test():
    return "studepimy API"


'''
    Final
'''


'''
    In Proc
'''



# Neuen Studenten erstellen
@app.route('/student',methods=['POST'])
def add_student():
    vorname = request.json['vorname']
    nachname=request.json['nachname']
    mail = request.json['mail']
    tel = request.json['tel']
    s=Student(vorname,nachname,mail,tel)# Test
    s.persist(db)
    studenten.append(s)
    return jsonify({"inserted":nachname+'('+str(s.id)+')'})


@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({"studenten":len(studenten)})

@app.route('/student/<sid>', methods=['GET'])
def get_student_by_studid(sid):
    if student_id_exitsts(sid) is True:
        s=get_student_by_id(sid)
        return jsonify(s.__dict__)
    else:
        return "Student existiert nicht!",400


'''
@app.route('/student/<nachname>', methods=['GET'])
def get_student_by_nachname(nachname):
    s=get_student_by_name(nachname)
    return jsonify(s.__dict__)
'''
@app.route('/student/<nachname>', methods=['PUT'])
def update_student(nachname):
    s=get_student_by_name(nachname)
    s.vorname=request.json['vorname']
    s.name=request.json['nachname']
    s.mail = request.json['mail']
    s.tel = request.json['tel']
    s.persist()
    return jsonify(s.__dict__)

#----------------------------------------------------------------------------------

@app.route('/hospital',methods=['POST'])
def add_hospital():
    #coordinates={'lat':0.0,'lan':0.0} # ToDO Klinik Locator
    #coordinates=kliniklocator.get_coordinates_by_name('MHH')

    h_name=request.json['name']
    h=Hospital(
        h_name,
        locator.get_ort_by_name(h_name),
        request.json['strasse'],
        request.json['hausnr'],
        request.json['plz'],
       # request.json['covid_patienten'],
        locator.get_coordinates_by_name(h_name)
    )
    h.persist()

    #studenten.append(s)
    return jsonify({"inserted":h.name}), 201

@app.route('/hospital', methods=['GET'])# umbennnen in Klinik o.ä ?
def get_hospital():
    return jsonify({"hospitals":len(hospitals)})


@app.route('/hospital/<name>', methods=['GET'])
def get_hospital_by_name(name):
    h=entity.get_hospital_by_name(name)
    return jsonify(h)

#----------------------------------------------------------------------------------
@app.route('/find_hospitals', methods=['GET'])
def find_hospitals():
    #stud_id=request.args.get('studid')
    #stud_id=99
    #stud=entity.get_student_by_id(stud_id)

    #result=entity.find_hospitals(stud,locator)

    location = {'lat': 52.375893, 'long': 9.732010}
    #loc_radius = 100000;
    #result=locator.get_hospitals_by_coordinates(la=location['long'],lo=location['lat'],radius=loc_radius)
    location = (52.375893, 9.732010)
    loc_radius = 10000;
    result = locator.get_hospitals_by_coordinates(location[0], location[1], loc_radius)

    return jsonify(result)
    #return jsonify({'found:':len(result)})
    #return jsonify(result)




if __name__ == '__main__':
    app.run()
