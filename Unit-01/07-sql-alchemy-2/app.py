from flask import Flask, request, url_for, redirect, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-messages-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

class User(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Text)
	first_name = db.Column(db.Text)
	last_name = db.Column(db.Text)
	messages = db.relationship('Message', backref = 'user', lazy='dynamic', cascade='all,delete')

	def __init__(self, username, first_name, last_name):
		self.username = username
		self.first_name = first_name
		self.last_name = last_name
	
	def __repr__(self):
		return "{}'s name is {} {}.".format(self.username, self.first_name, self.last_name)

class Message(db.Model):

	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, text, user_id):
		self.text = text
		self.user_id = user_id

@app.route('/')
def root():
	return render_template('users/index.html')

@app.route('/users')
def index():
	return render_template('users/index.html')

@app.route('/users/new')
def new():
	return render_template('users/new.html')

@app.route('/users/<int:id>')
def show(id):
	return render_template('users/show.html')

@app.route('/users/<int:id>/edit')
def edit(id):
	return render_template('users/edit.html')

@app.route('/users/<int:user_id>/messages')
def messages_index():
		pass

@app.route('/users/<int:user_id>/messages/new')
def messages_new(user_id):
	return render_template('messages/new.html')

@app.route('/users/<int:user_id>/messages/<int:id>')
def messages_show(user_id, id):
	pass

@app.route('/users/<int:user_id>/messages/<int:id>/edit')
def messages_edit(user_id, id):
	pass

if __name__ == '__main__':
	app.run(debug=True)	