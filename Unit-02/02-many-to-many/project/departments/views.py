from flask import redirect, render_template, request, url_for, Blueprint
from project.models import Department, Employee
from project.forms import NewDepartmentForm, DeleteForm
from project import db

departments_blueprint = Blueprint(
    'departments',
    __name__,
    template_folder='templates'
)

@departments_blueprint.route('/', methods = ['POST', 'GET'])
def index():
	form = NewDepartmentForm()
	if request.method == 'POST':
		new_department = Department(request.form['name'])
		db.session.add(new_department)
		db.session.commit()
		return redirect(url_for('departments.index'))
	return render_template('departments/index.html', departments = Department.query.all(), form=form)

@departments_blueprint.route('/new')
def new():
	form = NewDepartmentForm()
	return render_template('departments/new.html', form=form, departments=Department.query.all())	

@departments_blueprint.route('/<int:id>')
def show(id):
	found_department = Department.query.get(id)
	#employees = Department.employees.query.get(id)
	return render_template('departments/show.html', department = found_department)

@departments_blueprint.route('/<int:id>/edit')
def edit(id):
	found_department = Department.query.get(id)
	return render_template('departments/edit.html', department = found_department)		