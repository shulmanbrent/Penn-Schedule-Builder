import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from penn.registrar import Registrar

app = Flask(__name__, static_url_path='/static')

schedule_requirements = dict()


@app.route('/')
def main():
	return render_template("index.html")

@app.route("/scheduler", methods=['GET', 'POST'])
def scheduler():

	if request.method == 'POST':
		for (req, val) in request.form.items():
			schedule_requirements[req] =  val
		return render_template("restrictions.html")
	else:
		return render_template("port.html")

@app.route("/schedule", methods=['GET', 'POST'])
def restrictions():
	if request.method == 'POST':
		#TODO
	else:
		return render_template("restrictions.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)