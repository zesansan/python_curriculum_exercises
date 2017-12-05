from flask import redirect, render_template, request, url_for, Blueprint
from project.models import Department
from project.forms import NewEmployeeForm
from project import db

departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)

@departments_blueprint.route('/')
def index():
	return render_template('departments/index.html')

@departments_blueprint.route('/new')
def new():
	return render_template('departments/new.html')	

@departments_blueprint.route('/<int:id>')
def show(id):
	return render_template('departments/show.html')

@departments_blueprint.route('/<int:id>/edit')
def edit(id):
	return render_template('departments/edit.html')		