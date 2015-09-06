import jsonCourseParser as parser

# def course_meets_on_days(course, days_to_check):
# 	course_meeting_days = list(course["meetings_days"])
# 	for day_to_check in days_to_check:
# 		if day_to_check in course_meeting_days:
# 			return True
# 	return False

def courses_are_same(first_course, second_course):
	first_course_title = parser.get_course_department(first_course) \
		+ parser.get_course_number(first_course)
	second_course_title = parser.get_course_department(second_course) \
		+ parser.get_course_number(second_course)
	return first_course_title == second_course_title


def shared_meeting_days(first_course, second_course):
	first_course_meeting_days = parser.get_meetings(first_course).keys()
	second_course_meeting_days = parser.get_meetings(second_course).keys()
	days_overlapped = list()
	for meeting_day in first_course_meeting_days:
		if meeting_day in second_course_meeting_days:
			days_overlapped.append(meeting_day)
	return days_overlapped


def course_times_overlap(first_course_time, second_course_time):
	first_course_start = first_course_time[0]
	first_course_end = first_course_time[1]
	second_course_start = second_course_time[0]
	second_course_end = second_course_time[1]
	if first_course_start > second_course_start and \
		first_course_start < second_course_end:
		return True
	if second_course_start > first_course_start and \
		second_course_start < first_course_end:
		return True
	return False


def course_meeting_times_overlap(first_course, second_course, days_overlapped):
	first_course_meetings = parser.get_meetings(first_course)
	second_course_meetings = parser.get_meetings(second_course)
	for day in days_overlapped:
		first_course_times = first_course_meetings[day]
		second_course_times = second_course_meetings[day]
		for first_course_time in first_course_times:
			for second_course_time in second_course_times:
				if course_times_overlap(first_course_time, second_course_time):
					return True
	return False


def courses_overlap(first_course, second_course):
	if courses_are_same(first_course, second_course):
		return True
	else:
		shared_days = shared_meeting_days(first_course, second_course)
		if len(shared_days) == 0:
			return False
		return course_meeting_times_overlap(first_course, second_course, shared_days)

def filter_out_courses_that_overlap(first_course, courses_to_compare):
	courses_that_fit = list()
	for course_to_compare in courses_to_compare:
		if not courses_overlap(first_course, course_to_compare):
			courses_that_fit.append(course_to_compare)
	return courses_that_fit


def get_least_difficult_course(all_courses):
	least_diffcult = all_courses[0]
	for course in all_courses:
		if course["course_difficulty"] < least_diffcult["course_difficulty"]:
			least_diffcult = course
	return least_diffcult


def pick_best_schedule(all_courses, number_of_courses_to_take):
	schedule = list()
	courses_that_fit = all_courses
	while (schedule.len() < number_of_courses_to_take and courses_that_fit.len() > 0):
		least_difficult_course = get_least_difficult_course(courses_that_fit)
		schedule.append(least_difficult_course)
		courses_that_fit = filter_out_courses_that_overlap(least_difficult_course, courses_that_fit)
	return schedule

def filter_out_courses_that_overlap(first_course, courses_to_compare):
	courses_that_fit = list()
	for course_to_compare in courses_to_compare:
		if not courses_overlap(first_course, course_to_compare):
			courses_that_fit.append(course_to_compare)
	return courses_that_fit





