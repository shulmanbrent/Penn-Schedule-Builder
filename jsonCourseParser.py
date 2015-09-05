
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

def get_meetings(course):
	
