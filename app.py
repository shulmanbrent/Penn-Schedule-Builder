import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from penn.registrar import Registrar

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
	return render_template("index.html")

@app.route("/scheduler")
def scheduler():
	courses = open("class_list.txt", 'r')
	classes = courses.readline()
	return render_template("scheduler.html", classes=classes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)