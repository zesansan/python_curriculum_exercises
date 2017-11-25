from flask import Flask, request, render_template, url_for, redirect
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

@app.route('/snacks', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		new_snack = Snack(
			request.form.get('snack_name'), 
			request.form.get('snack_kind')
			)
		snacks.append(new_snack)
		return redirect(url_for('index'))	
	return render_template('index.html', snacks=snacks)

@app.route('/snacks/new')
def new():
	return render_template('new.html')

@app.route('/snacks/<int:id>', methods=['GET', 'DELETE', 'PATCH'])
def show(id):

	found_snack = [
		snack 
		for snack in snacks 
		if snack.id == id
	][0]

	if request.method == b'PATCH':
		found_snack.name = request.form.get('snack_name')

	if request.method == b'DELETE': 
		snacks.remove(found_snack)

	if found_snack and request.method == 'GET':	
		return render_template('show.html', snack=found_snack)
	return redirect(url_for('index'))	

@app.route('/snacks/<int:id>/edit')

def edit(id):
	found_snack = [
		snack 
		for snack in snacks 
		if snack.id == id
		][0]
	
	return render_template('edit.html', snack=found_snack)			

if __name__ == '__main__':
	app.run(debug=True)	

		