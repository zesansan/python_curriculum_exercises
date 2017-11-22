from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/home")
def home():
	return render_template("index.html")

@app.route("/add")
def add():
	return render_template("add.html")

@app.route("/subtract")
def subract():
	return render_template("subract.html")

@app.route("/multiply")
def multiply():
	return render_template("multiply.html")

@app.route("/divide")
def divide():
	return render_template("divide.html")

if __name__=="__main__":
	app.run(debug=True)