from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/many-to-many-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MOVE ME TO AN ENV FILE!'
db = SQLAlchemy(app)
modus = Modus(app)

from project import db

EmployeeDepartment = db.Table('emplyee_departments', 
								db.Column('id',
											db.Integer,
											primary_key=True),
								db.Column('employee_id', 
											db.Integer,
											db.ForeignKey('employees.id', ondelete="cascade")),
								db.Column('department_id',
											db.Integer,
											db.ForeignKey('departments.id', ondelete="cascade")))
class Employee(db.Model):
	__tablename__ ='employees'

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.Text)
	years_at_company = db.Column(db.Integer)
	departments = db.relationship("Department",
									secondary=EmployeeDepartment,
									backref=db.backref('employees'))

	def __init__(self,name,years_at_company):
		self.name = name
		self.years_at_company = years_at_company

	def __repr__(self):
		return "{} has been at the company for {} years.".format(self.name,self.years_at_company)

class Department(db.Model):
	__tablename__ = 'departments'

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.Text)

	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return "{} is the deparment.".format(self.name)	

