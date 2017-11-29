from flask import Flask, request, url_for, redirect, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/users-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
modus = Modus(app)

@app.route('/users')
def index():
	return render_template('index.html')

@app.route('/users/new')
def new():
	return render_template('new.html')

@app.route('/users/<in:user_id>')
def show(user_id):
	return render_template('show.html')

@app.route('/users/<in:user_id>/edit')
def edit(user_id):
	return render_template('edit.html')			

if __name__ == '__main__':
	app.run(debug=True)	