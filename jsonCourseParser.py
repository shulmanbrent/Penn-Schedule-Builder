
def get_course_department(course):
	department = course['course_department']
	return department.encode('ascii')

def get_course_number(course):
	number = course['course_number']
	return number.encode('ascii')

def get_credits(course):
	credits = course['credits']
	credits = credits.encode('ascii')
	credits_parsed = credits[:3]
	return float(credits_parsed)

def get_section(course):
	section = course['section_number']
	return section.encode('ascii')

def get_requirements(course):
	requirements = course['fulfills_college_requirements']
	return convert_to_ascii(requirements)

def get_meetings(course):
	day_map = {}
	meetings = course['meetings']

	for meeting in meetings:

		days = list(meeting['meeting_days'].encode('ascii'))

		start_time = meeting['start_time_24']
		end_time = meeting['end_time_24']

		for day in days:
			if day not in day_map:
				day_map[day] = []

			day_map[day].append((start_time, end_time))

	return day_map

def convert_to_ascii(string_list):
	for i in range(0, len(string_list)):
		string_list[i] = string_list[i].encode('ascii')

def get_prereqs(course):
	prereq_notes = course['prerequisite_notes']
	if len(prereq_notes) == 0:
		return list()
	prereqs = prereq_notes[0].split(", ")
	return prereqs


