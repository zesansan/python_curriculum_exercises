from flask import Blueprint, redirect, render_template, url_for, request
from project.users.models import User
from project.users.forms import UserForm, DeleteForm, LoginForm
from project import db

from sqlalchemy.exc import IntegrityError
users_blueprint = Blueprint('users', __name__, template_folder='templates')

@users_blueprint.route('/signup', methods =["GET", "POST"])
def signup():
    form = UserForm(request.form)
    if request.method == "POST" and form.validate():
        try:
            new_user = User(form.data['username'],
            				form.data['password'],
            				form.data['first_name'],
            				form.data['last_name'])
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError as e:
            return render_template('users/signup.html', form=form)
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        if User.authenticate(form.data['username'], form.data['password']):
            return redirect(url_for('users.welcome'))
    return render_template('users/login.html', form=form)

@users_blueprint.route('/welcome')
def welcome():
    return render_template('users/welcome.html')

# @users_blueprint.route('/', methods=['POST', 'GET'])
# def index():
# 	if request.method=='POST':
# 		form = UserForm(request.form)
# 		if form.validate():
# 			new_user = User(request.form['username'],request.form['first_name'],request.form['last_name'])
# 			db.session.add(new_user)
# 			db.session.commit()
# 			flash('User created!')
# 			return redirect(url_for('users.index'))	
# 		return render_template('new.html', form=form)	
# 	return render_template('index.html', users=User.query.all())

# @users_blueprint.route('/new')
# def new():
# 	user_form = UserForm()
# 	return render_template('new.html', form=user_form)

# @users_blueprint.route('/<int:id>', methods=['GET','PATCH','DELETE'])
# def show(id):
# 	found_user = User.query.get(id)
# 	if request.method == b'PATCH':
# 		form = UserForm(request.form)
# 		if form.validate():
# 			found_user.username = form.username.data
# 			found_user.first_name = form.first_name.data
# 			found_user.last_name = form.last_name.data
# 			db.session.add(found_user)
# 			db.session.commit()
# 			flash('User updated!')
# 			return redirect(url_for('users.index'))
# 		return render_template('edit.html', user=found_user, form=form)	
# 	if request.method ==b'DELETE':
# 		form = DeleteForm(request.form)
# 		if form.validate():
# 			db.session.delete(found_user)
# 			db.session.commit()
# 			flash('User deleted!')
# 		return redirect(url_for('users.index'))
# 	return render_template('show.html', user=found_user, delete_form=form)

# @users_blueprint.route('/<int:id>/edit')
# def edit(id):
# 	user=User.query.get(id)
# 	user_form = UserForm(obj=user) #use obj to prepopulate forms
# 	return render_template('edit.html', user=user, form=user_form)	


