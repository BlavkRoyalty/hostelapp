
import json
from flask import make_response,url_for, request,jsonify
from flask.helpers import make_response
from werkzeug.datastructures import auth_property
from werkzeug.wrappers import response
from projectapp.mymodel import Hostel,db,Merchant
from flask import render_template,url_for,session
from flask_httpauth import HTTPBasicAuth


# import the blueprint's instance
from . import apiobj


auth = HTTPBasicAuth()
def get_password(username):
    deets = db.session.query(Merchant.mer_pwd).filter(Merchant.mer_username==username).first()   
    if deets:
        return deets.password

    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error':'Unauthorized access'}), 401) 


#FETCH ALL hostel -GET
@apiobj.route('/list/')
# @csrf.exempt

#GET
def listall(): 
    hostels = []
    data = Hostel.query.filter().all()
    for x in data:
        a ={}
        a['hostel'] = x.hostel_name
        a['type'] = x.hostel_type
        a['desc'] = x.hostel_desc
        hostels.append(a)
    return jsonify(hostels)



#get details of one hostel -GET
@apiobj.route('/list/<int:hostel_id>')
@auth.login_required
def listone(hostel_id): 
    data = Hostel.query.filter(Hostel.hostel_id==hostel_id).first()
    data2send = {"hostel":data.hostel_name,"type":data.hostel_type}
    rsp = make_response(json.dumps(data2send), 200)
    rsp.headers['Content-Type']="application/json"
    return json.dumps(data2send)



#add new hostel details - GET
@apiobj.route('/addnew/', methods=['POST'])
def update(): 
    return 'Hostel Added successfully'
#delete hostel details - POST
@apiobj.route('/deletehostel/<int:hostel_id>', methods=['DELETE'])
def deletehostel(hostel_id): 
        data = Hostel.query.filter(Hostel.hostel_id==hostel_id).first()
        data2send = {"hostel":data.hostel_name,"type":data.hostel_type}
        rsp = make_response(json.dumps(data2send), 200)
        rsp.headers['Content-Type']="application/json"
        return 'Hostel Deleted'
        
#UpdateQ hostel details - Post
@apiobj.route('/addnew/', methods=['POST'])
def addnew(): 
    if request.is_json:
        hostel_deets = response.get_json()
        hostelname = hostel_deets['hostelname']
        desc = hostel_deets['description']
        hosteltype = hostel_deets['type']
        host = Hostel(hostel_name = hostelname, hostel_desc = desc, hostel_type = hosteltype)
        db.session.add(host)
        db.session.commit()
        return f'{hostelname} is Successfully Added'
        # ret = {"status":1, "msg": 'Hostel added'}
        # return 'ret'

    else:
        # ret = {"status" : 0, "msg": 'Try Again'}
        return "kiniiiiiii"
