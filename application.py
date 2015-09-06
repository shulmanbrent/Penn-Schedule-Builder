import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from penn.registrar import Registrar
import flask
from pennScheduleBuilder import ScheduleBuilder
from jsonCourseParser import get_meetings

app = Flask(__name__, static_url_path='/static')

schedule_requirements = dict()
sb = ScheduleBuilder()

flask.debug= True

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
			if val != u'0' and ('required-class' not in req) and ('taken-class' not in req):
				schedule_requirements[req] =  int(val)
		return render_template("restrictions.html")
	else:
		return render_template("scheduler.html")

@app.route("/your_schedule", methods=['GET', 'POST'])
def restrictions():
	if request.method == 'POST':


		schedule_requirements
		sb.set_requirements(schedule_requirements)
		dotw = list()
		for (req, val) in request.form.items():
			if req == 'dotw':
				dotw.append(val)
		
		sb.enter_preferences(no_class_days=dotw)
		schedule = sb.find_schedule()
		my_data = list()
		for i, course in enumerate(schedule):
			temp = dict()
			temp['full_name'] = course['meetings'][0]['section_id_normalized']
			temp['meetings'] = get_meetings(course)
			my_data.append(temp)
		print my_data
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
		class_bd = class_by_days(my_data)
		# print class_bd
		print "about to render_template"
		return render_template("your-schedule.html", data=my_data, by_date=class_bd)
	else:
		return render_template("index.html")

def class_by_days(data):
	by_day = {"M": list(), "T": list(), "W": list(), "R": list(), "F": list()}
	for c in data:
		for day, time in c["meetings"].items():
			by_day[day].append(c)
	for day in by_day:
		sorted(by_day[day], key=lambda c: c["meetings"].itervalues().next()[0][0])
	# print "rturning"
	return by_day

def class_exists(form):
	possible_classes = open("class_list.txt", 'r')
	for k, v in form.items():
		if "required-class" in k or "taken-class" in k:
			if any([v == name[:-1] for name in possible_classes]):
				continue
			else:
				possible_classes.close()
				return v
	possible_classes.close()
	return None


if __name__ == '__main__':
    app.run()