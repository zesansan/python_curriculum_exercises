from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/many-to-many-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
modus = Modus(app)

from project.employees.views import employees_blueprint
from project.departments.views import departments_blueprint

app.register_blueprint(employees_blueprint, url_prefix='/employees')
app.register_blueprint(departments_blueprint, url_prefix='/departments')

@app.route('/')
def root():
	return redirect(url_for('employees.index'))

