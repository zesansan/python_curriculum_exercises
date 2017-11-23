from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/home")
def index():
	return render_template("index.html")

@app.route("/add/", methods = ["GET", "POST"])
def add():
	
	if request.method == "POST":
		num1 = int(request.form['add_num1'])
		num2 = int(request.form['add_num2'])
		add_result = num1 + num2
		return render_template("add.html", add_result = add_result)
	elif request.method == 'GET':
		return render_template("add.html")

@app.route("/subtract/", methods =['GET', 'POST'])
def subtract():
	if request.method == "POST":
		num1 = int(request.form['sub_num1'])
		num2 = int(request.form['sub_num2'])
		sub_result = num1 - num2
		return render_template("subtract.html", sub_result = sub_result)
	elif request.method == 'GET':
		return render_template("subtract.html")

@app.route("/multiply", methods =['GET', 'POST'])
def multiply():
	if request.method == "POST":
		num1 = int(request.form['mult_num1'])
		num2 = int(request.form['mult_num2'])
		mult_result = num1 * num2
		return render_template("multiply.html", mult_result = mult_result)
	elif request.method == 'GET':
		return render_template("multiply.html")

@app.route("/divide/", methods =['GET', 'POST'])
def divide(divide_num1, divide_num2):
	if request.method == "POST":
		num1 = int(request.form['divide_num1'])
		num2 = int(request.form['divide_num2'])
		divide_result = num1 / num2
		return render_template("divide.html", divide_result = divide_result)
	elif request.method == 'GET':
		return render_template("divide.html")
