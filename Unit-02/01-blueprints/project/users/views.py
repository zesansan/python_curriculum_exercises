from flask import Blueprint, redirect, render_template, url_for, request
from project.users.models import User
from project.users.forms import UserForm, DeleteForm
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='templates/users')

@users_blueprint.route('/users', methods=['POST', 'GET'])
def index():
	if request.method=='POST':
		form = UserForm(request.form)
		if form.validate():
			new_user = User(request.form['username'],request.form['first_name'],request.form['last_name'])
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('users.index'))	
		else:
			return render_template('user/new.html', form=form)	
	return render_template('users/index.html', users=User.query.all())

@users_blueprint.route('/users/new')
def new():
	user_form = UserForm()
	return render_template('users/new.html', form=user_form)

@users_blueprint.route('/users/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
	found_user = User.query.get(id)
	if request.method == b'PATCH':
		form = UserForm(request.form)
		if form.validate():
			found_user.username = form.username.data
			found_user.first_name = form.first_name.data
			found_user.last_name = form.last_name.data
			db.session.add(found_user)
			db.session.commit()
			return redirect(url_for('users.index'))
		return render_template('users/edit.html', user=found_user, form=form)	
	if request.method ==b'DELETE':
		delete_form = DeleteForm()
		if delete_form.validate():
			db.session.delete(found_user)
			db.session.commit()
		return redirect(url_for('users.index'))
	return render_template('users/show.html', user=found_user)

@users_blueprint.route('/users/<int:id>/edit')
def edit(id):
	delete_form = DeleteForm()
	user=User.query.get(id)
	user_form = UserForm(obj=user) #use obj to prepopulate forms
	return render_template('users/edit.html', user=user, form=user_form,delete_form=delete_form)	