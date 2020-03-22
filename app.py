from flask import Flask
from flask import request
from flask import jsonify
from flask_swagger import swagger
from entity import *
import entity
from clinic_locator import ClinicLocator

import PersistenceTest

PersistenceTest.testDB()
__author__='Max'
__status__='DEV'


app = Flask(__name__)
locator=ClinicLocator()

@app.route('/')
def test():
    return "studepimy API"

@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)

@app.route('/student',methods=['POST'])
def add_student():
    vorname = request.json['vorname']
    nachname=request.json['nachname']
    mail = request.json['mail']
    tel = request.json['tel']
    s=Student(vorname,nachname,mail,tel)# Test
    s.persist()
    #studenten.append(s)
    return jsonify({"inserted":nachname})

@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({"studenten":len(studenten)})

@app.route('/student/<nachname>', methods=['GET'])
def get_student_by_nachname(nachname):
    s=get_student_by_name(nachname)
    return jsonify(s.__dict__)

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
        request.json['covid_patienten'],
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






if __name__ == '__main__':
    app.run()
