import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from penn.registrar import Registrar

app = Flask(__name__, static_url_path='/static')

schedule_requirements = dict()


@app.route('/')
def main():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/scheduler", methods=['GET', 'POST'])
def scheduler():

	if request.method == 'POST':
		bad_class = class_exists(request.form)
		if bad_class:
			return render_template("scheduler.html", bad_class=bad_class)
		for (req, val) in request.form.items():
			schedule_requirements[req] =  val
		return render_template("restrictions.html")
	else:
		return render_template("scheduler.html")

@app.route("/your_schedule", methods=['GET', 'POST'])
def restrictions():
	if request.method != 'POST':
		for (req, val) in request.form.items():
			schedule_requirements[req] =  val
		sample_data = [
						{
						"full_name": "NETS 212",
						"requirement_filled": "Arts and Letters",
						"meetings": {
									"days": ["Tuesday", "Thursday"],
									"tod": [12, 13.5]
								  }
						},
						{
						"full_name": "CIS 110",
						"requirement_filled": "Physical World",
						"meetings": {
									"days": ["Monday", "Wednesday", "Friday"],
									"tod": [11, 12]
								  }
						},
						{
						"full_name": "Span 130",
						"requirement_filled": "Something",
						"meetings": {
									"days": ["Monday", "Tuesday", "Wednesday", "Friday"],
									"tod": [12, 13]
								  }
						}
					]
		class_bd = class_by_days(sample_data)
		print "about to render_template"
		return render_template("your-schedule.html", data=sample_data, 	by_date=class_bd)
	else:
		return render_template("your-schedule.html")

def class_by_days(data):
	by_day = {"Monday": list(), "Tuesday": list(), "Wednesday": list(), "Thursday": list(), "Friday": list()}
	for c in data:
		for day in c["meetings"]["days"]:
			print "MOFO"
			by_day[day].append(c)
	for day in by_day:
		print "By day"
		sorted(by_day[day], key=lambda c: c["meetings"]['tod'][0])
	print "returning"
	return by_day

def class_exists(form):
	possible_classes = open("class_list.txt", 'r')
	for k, v in form.items():
		if "required-class" in k or "taken-class" in k:
			if any([v == name[:-1] for name in possible_classes]):
				continue
			else:
				return v


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)