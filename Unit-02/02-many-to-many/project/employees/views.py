from flask import redirect, render_template, request, url_for, Blueprint
from project.models import Employee, Department
from project.forms import NewEmployeeForm, DeleteForm
from project import db

employees_blueprint = Blueprint(
    'employees',
    __name__,
    template_folder='templates'
)

@employees_blueprint.route('/', methods = ['GET', 'POST'])
def index():
	form= NewEmployeeForm()
	form.set_choices()
	if request.method == 'POST':
		new_employee = Employee(request.form['name'],
								request.form['years_at_company']
								)
		for department in form.departments.data:
			new_employee.departments.append(Department.query.get(department))
		db.session.add(new_employee)
		db.session.commit()
		return redirect(url_for('employees.index'))	
	return render_template('employees/index.html', employees = Employee.query.all(), form=form)

@employees_blueprint.route('/new')
def new():
	form = NewEmployeeForm()
	form.set_choices()
	return render_template('employees/new.html', form=form)

@employees_blueprint.route('/<int:id>', methods=['PATCH','DELETE','GET'])
def show(id):
	found_employee = Employee.query.get(id)
	form = NewEmployeeForm(request.form)
	delete_form = DeleteForm()
	form.set_choices()
	if request.method == b'PATCH':
		if form.validate():
			found_employee.name = request.form['name']	
			found_employee.years_at_company = request.form['years_at_company']
			found_employee.departments = []
			for department in form.departments.data:
				found_employee.departments.append(Department.query.get(department))
			db.session.add(found_employee)	
			db.session.commit()
			return redirect(url_for('employees.show', id=id))
	if request.method == b'DELETE':
		db.session.delete(found_employee)
		db.session.commit()
		return redirect(url_for('employees.index'))
	return render_template('employees/show.html', employee=found_employee, form=form, delete_form=delete_form)

@employees_blueprint.route('/<int:id>/edit')
def edit(id):
	found_employee = Employee.query.get(id)
	form = NewEmployeeForm(request.form)
	delete_form = DeleteForm()
	form.set_choices()
	return render_template('employees/edit.html', employee = found_employee, form=form, delete_form=delete_form)
