from flask import Flask, render_template, url_for
from snack import Snack
from flask_modus import Modus

snacks=[
	Snack('potato chips', 'savory'),
	Snack('beef jerky', 'savory'),
	Snack('chocolate chip cookies', 'sweet'),
	Snack('granola bar', 'health')

]

app = Flask(__name__)
modus = Modus(app)

@app.route('/snacks', methods=["GET", "POST"])
def index():
	return render_template('index.html', snacks = snacks)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/:id')
def show():
	return render_template('show.html')

@app.route('/snacks/:id/edit')
def edit():
	return render_template('edit.html')			

if __name__ == '__main__':
	app.run(debug=True)	

		