import jsonCourseParser as parser

def courses_are_same(first_course, second_course):
	first_course_title = first_course["course_department"] 
		+ first_course["course_number"]
	second_course_title = second_course["course_department"] 
		+ second_course["course_number"]
	return first_course_title == second_course_title


def courses_share_meeting_days(first_course, second_course):
	first_course_meeting_days = list(first_course["meeting_days"])
	second_course_meeting_days = list(second_course["meeting_days"])
	for meeting_day in first_course_meeting_days:
		if meeting_day in second_course_meeting_days:
			return true
	return false


def course_meeting_times_overlap(first_course, second_course):
	first_course_start_time = first_course["start_time_24"]
	first_course_end_time = first_course["end_time_24"]
	second_course_start_time = second_course["start_time_24"]
	second_course_end_time = second_course["end_time_24"]
	if first_course_start_time > second_course_start_time 
		and first_course_start_time < second_course_start_time:
		return true
	if second_course_start_time > first_course_start_time 
		and second_course_start_time < first_course_start_time:
		return true
	return false


def courses_overlap(first_course, second_course):
	if courses_are_same(first_course, second_course):
		return true
	else:
		return courses_share_meeting_days(first_course, second_course) and
			course_meeting_times_overlap(first_course, second_course)


def filter_out_courses_that_overlap(first_course, courses_to_compare):
	courses_that_fit = list()
	for course_to_compare in courses_to_compare:
		if not courses_overlap(first_course, course_to_compare):
			courses_that_fit.append(course_to_compare)
	return courses_that_fit


#def get_least_difficult_course(all_courses):
#	least_diffcult = all_courses[0]
#	for course in all_courses:
#		if course["course_difficulty"] < least_diffcult["course_difficulty"]:
#			least_diffcult = course
#	return least_diffcult


#def pick_best_schedule(all_courses, number_of_courses_to_take):
#	schedule = list()
#	courses_that_fit = all_courses
#	while (schedule.len() < number_of_courses_to_take and courses_that_fit.len() > 0):
#		least_difficult_course = get_least_difficult_course(courses_that_fit)
#		schedule.append(least_difficult_course)
#		courses_that_fit = filter_out_courses_that_overlap(least_difficult_course, courses_that_fit)
#	return schedule
		

def course_meets_on_days(course, days_to_check):
	course_meeting_days = list(course["meetings_days"])
	for day_to_check in days_to_check:
		if day_to_check in course_meeting_days:
			return true
	return false





