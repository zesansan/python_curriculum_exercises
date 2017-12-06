from flask import Blueprint, redirect, render_template, url_for, request, session, flash, g 
from project.users.models import User
from project.users.forms import UserForm, DeleteForm, LoginForm
from functools import wraps
from project import db, bcrypt

from sqlalchemy.exc import IntegrityError
users_blueprint = Blueprint('users', __name__, template_folder='templates')

def ensure_logged_in(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            flash("Please log in first, fren.")
            return redirect(url_for('users.login'))
        return fn(*args, **kwargs)
    return wrapper 

def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('id') != session.get('user_id'):
            flash("Not Authorized, fren.")
            return redirect(url_for('users.welcome'))
        return fn(*args, **kwargs)
    return wrapper       

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
            flash("Invalid submission. Please try again.")
            return render_template('users/signup.html', form=form)
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.authenticate(form.data['username'], form.data['password'])
        if user:
            session['user_id'] = user.id
            flash("You've successfully logged in!")
            return redirect(url_for('users.welcome'))
        flash("Invalid credentials. Please try again.")
    return render_template('users/login.html', form=form)

@users_blueprint.before_request
def current_user():
    if session.get('user_id'):
        g.current_user= User.query.get(session['user_id'])
    else:
        g.current_user = None    

@users_blueprint.route('/welcome')
@ensure_logged_in
def welcome():
    return render_template('users/welcome.html', users=User.query.all())

@users_blueprint.route('/logout')    
def logout():
    session.pop('user_id', None)
    flash('You have been logged out, fren.')
    return redirect(url_for('users.login'))

@users_blueprint.route('/<int:id>', methods=['GET','PATCH','DELETE'])
def show(id):
    found_user = User.query.get(id)
    if request.method == b'PATCH':
    	form = UserForm(request.form)
    	if form.validate():
            found_user.username = form.username.data
            found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            found_user.first_name = form.first_name.data
            found_user.last_name = form.last_name.data
            db.session.add(found_user)
            db.session.commit()
            flash('User updated!')
            return redirect(url_for('users.welcome'))
            return render_template('users/edit.html', user=found_user, form=form)	
    if request.method ==b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
        	db.session.delete(found_user)
        	db.session.commit()
        	flash('User deleted!')
        return redirect(url_for('users.welcome'))
        return render_template('users/show.html', user=found_user, delete_form=form)

@users_blueprint.route('/<int:id>/edit')
@ensure_logged_in
@ensure_correct_user
def edit(id):
	user=User.query.get(id)
	user_form = UserForm(obj=user) #use obj to prepopulate forms
	return render_template('users/edit.html', user=user, form=user_form)	


