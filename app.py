from flask import Flask
from flask import request
from flask import jsonify
import flask_login
from flask_swagger import swagger
from entity import *
import entity
from clinic_locator import ClinicLocator
from persistence.DBController import DBController
__author__='Max'
__status__='DEV'

'''
    Final
'''
app = Flask(__name__)
app.secret_key = 'test123'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)



@app.route('/login', methods=['GET', 'POST'])
def login():
    email= request.json['email']
    pw=request.json['password']

    auth_check=db.student_exists(email,pw)
    #if auth_check is False:
    #    auth_check=db.hospital_exists(email,pw)

    if auth_check is False:
        return "Bad Login"
    else:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return 'Login'

locator=ClinicLocator()
db=DBController("sqlite3")


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'
@app.route('/')
def root():
    return 'medsupport Webservice'


#Krankenhaus einfuegen
@app.route('/hospital',methods=['POST'])
def add_hospital():
    #coordinates={'lat':0.0,'lan':0.0} # ToDO Klinik Locator
    #coordinates=kliniklocator.get_coordinates_by_name('MHH')

    h_name=request.json['name']
    #(self, name, ort, strasse, plz, gesucht, coordinates, vorname, nachname, mail, tel, pw)
    h=Hospital(
        h_name,
        ort=locator.get_ort_by_name(h_name),
        strasse=locator.get_strasse_by_name(h_name),
        plz=locator.get_plz_by_name(h_name),
        gesucht=int(request.json['gesucht']),
        coord=locator.get_coordinates_by_name(h_name),
        vorname=request.json['vorname'],
        nachname=request.json['nachname'],
        mail=request.json['mail'],
        tel=request.json['tel'],
        pw=request.json['pw']
    )
    h.persist(db)
    return jsonify({"inserted": h_name + '(' + str(h.id) + ')'})

    #studenten.append(s)
    return jsonify({"inserted":h.name}), 201

# Neuen Studenten erstellen
@app.route('/student',methods=['POST'])
def add_student():
    vorname = request.json['vorname']
    nachname=request.json['nachname']
    mail = request.json['mail']
    tel = request.json['tel']
    coordinates={'long': float(request.json['long']), 'lat': float(request.json['lat'])}

    semester=request.json['semester']
    pw=request.json['pw']
    s=Student(vorname=vorname, name=nachname, mail=mail,tel=tel,coord=coordinates,semester=semester,pw=pw)

    s.persist(db)
    return jsonify({"inserted":nachname+'('+str(s.id)+')'})


# ----------------------------------------------------------------------------------
# Krankenhaueser in der Region finden
@app.route('/find_hospitals', methods=['GET'])
def find_hospitals():
    stud_id = request.args.get('studid')

    location = db.get_student_location(stud_id)

    loc_radius = 10000;
    result = locator.get_hospitals_by_coordinates(location[1], location[0], loc_radius)

    return jsonify(result)
'''
    In Proc
'''


class User(flask_login.UserMixin):
    pass
@login_manager.user_loader
def load_user(user_id):
    db.get_person_id(email)
    return
    #return User.get(user_id)



'''
@app.route('/student', methods=['GET'])
def get_student():
    return jsonify({"studenten":len(studenten)})
'''

'''
@app.route('/student/<sid>', methods=['GET'])
def get_student_by_studid(sid):
    if student_id_exitsts(sid) is True:
        s=get_student_by_id(sid)
        return jsonify(s.__dict__)
    else:
        return "Student existiert nicht!",400

'''
'''
@app.route('/student/<nachname>', methods=['GET'])
def get_student_by_nachname(nachname):
    s=get_student_by_name(nachname)
    return jsonify(s.__dict__)
'''

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
'''
#----------------------------------------------------------------------------------
'''
@app.route('/hospital', methods=['GET'])# umbennnen in Klinik o.ä ?
def get_hospital():
    return jsonify({"hospitals":len(hospitals)})


@app.route('/hospital/<name>', methods=['GET'])
def get_hospital_by_name(name):
    h=entity.get_hospital_by_name(name)
    return jsonify(h)

'''




if __name__ == '__main__':
    app.run()
