from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculator")
def calc():
		return render_template("calc.html")

@app.route("/math", methods =['POST'])
def math():
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	if request.form['math']=='add': 
		return "the sum is {}".format(num1 + num2)
	elif request.form['math'] == 'subtract':
		return "the difference is {}".format(num1 - num2)
	elif request.form['math'] == 'multiply':
		return "the product is {}".format(num1 * num2)
	elif request.form['math'] == 'divide':
		return "the quotient is {}".format(num1 / num2)			

@app.route("/person/<name>/<int:age>")
def person(name, age):
	name = name
	age = age
	response = "Hello, {}. You are {} years old.".format(name, age)	
	return render_template("person.html", response = response)

if __name__=="__main__":
	app.run(debug=True)
