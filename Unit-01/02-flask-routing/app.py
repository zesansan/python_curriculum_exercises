from flask import Flask

app = Flask(__name__)

@app.route("/add/<int:add_num1>/<int:add_num2>")
def add(add_num1, add_num2):
	return "The sum is {}".format(add_num1 + add_num2)

@app.route("/subtract/<int:subtract_num1>/<int:subtract_num2>")
def subtract(subtract_num1, subtract_num2):
		return "The difference is {}".format(subtract_num1 - subtract_num2) 

@app.route("/multiply/<int:mult_num1>/<int:mult_num2>")
def multiply(mult_num1, mult_num2):
	return "The product is {}".format(mult_num1 * mult_num2)

@app.route("/divide/<int:divide_num1>/<int:divide_num2>")
def divide(divide_num1, divide_num2):
	return "The quotient is {}".format(divide_num1 / divide_num2)

@app.route("math/")
def math(math_add_num1, math_add_num2):
	return "The sum is {}".format(math_add_num1 + math_add_num2)

if __name__=="__main__":
	app.run(debug=True)


