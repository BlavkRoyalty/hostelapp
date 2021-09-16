from datetime import datetime
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hostel(db.Model):
   
    hostel_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    hostel_name =  db.Column(db.String(255), nullable=False)
    hostel_desc = db.Column(db.String(255), nullable=False)
    hostel_type =  db.Column(db.Enum('Female','Male','Mixed'))
    hostel_dateadded = db.Column(db.DateTime(),default=datetime.datetime.utcnow)


class Merchant(db.Model):
    mer_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    mer_username =  db.Column(db.String(50), nullable=False)
    mer_pwd = db.Column(db.String(55), nullable=True)

