from penn.registrar import Registrar
import json
import os
import penncoursereview
import jsonCourseParser as CourseParser
import courseComparator
import pdb

class ScheduleBuilder(object):

	def __init__(self):
		self.registrar = Registrar('UPENN_OD_emFc_1001364', '6kl4eonkquheuti65e32qick6l')
		os.environ['PCR_AUTH_TOKEN']='kdutFhMEbUaKdvQbcRKszEiwZeThFs'


	def set_requirements(self, reqs):
		if reqs == None or len(reqs) == 0:
			return 'Must have at least one requirement'

		total_credits = 0
		for req in reqs:
			total_credits = total_credits + reqs[req]
		
		if total_credits > 6.5:
			return 'Why the fuck are you taking more than six and a half classes, go outside'

		self.req_numbers = reqs
		return True
		

	def find_all_courses(self, req_type, course_level_above=None, course_level_below=None, starts_after=None):
		# First enter default params for all courses

		print "Finding classes with params: "

		search_params = {}
		search_params['fulfills_requirement'] = req_type
		search_params['term'] = '2015C'
		search_params['status'] = 'O'
		search_params['is_cancelled'] = False
		# if course_level_above is not None:
		# 	search_params['course_level_above'] = course_level_above
		# if course_level_below is not None:
		# 	search_params['course_level_below'] = course_level_below
		# if starts_after is not None:
		# 	search_params['starts_at_or_after_hour'] = starts_after

		all_courses = self.registrar.search(search_params)

		print "request finished"

		return all_courses

	# def add_ratings(courses):
	# 	for course in courses:
	# 		course_info = penncoursereview(CourseParser.get_course_department(course), CourseParser.get_course_number(course), \
	# 			CourseParser.get_section(course))

	# 		difficulty_rating = course_info./


	def enter_preferences(self, starts_after=None, ends_before=None, no_class_days=None, difficulty_limit=None, work_limit=None, lunch_break=None):
		self.all_valid_courses = []

		for req in self.req_numbers:
			self.all_valid_courses = self.all_valid_courses + self.generator_to_list(self.find_all_courses(req, starts_after=starts_after))
		
		if no_class_days is not None:
			self.filter_course_days(self.all_valid_courses, no_class_days)
		self.all_valid_courses.sort(self.cmp_course)


	def cmp_course(self, course1, course2):

		if len(course1['meetings']) == 0 and len(course2['meetings']):
			return 0
		elif len(course1['meetings']) == 0:
			return 1
		elif len(course2['meetings']) == 0:
			return -1

		start_time1 = course1['meetings'][0]['start_time_24']
		start_time2 = course2['meetings'][0]['start_time_24']

		if start_time1 < start_time2:
			return -1
		elif start_time2 < start_time1:
			return 1
		else:
			return 0

	def filter_course_days(self, courses, no_class_days):
		for i in range(0, len(courses) - 1):
			current_course = courses[i]
			if courseComparator.course_meets_on_days(current_course, no_class_days):
				del current_course[i]

	def find_schedule(self):

		result = self.find_schedule_recurse(self.all_valid_courses, self.req_numbers, [])


		return result

	def find_schedule_recurse(self, all_courses, req_numbers, selected_classes):

		if self.total_reqs_remaining(req_numbers) == 0:
			return selected_classes
		elif len(all_courses) == 0:
			return False

		for i in range(0, len(all_courses) - 1):

			print i
			course_to_add = all_courses[i]

			# if course is not needed in requirements
			all_course_reqs = CourseParser.get_requirements(course_to_add)

			if course_to_add not in all_course_reqs:
				continue

			selected_classes.append(course_to_add)

			courses_after_selected = all_courses[i:]

			all_courses = courseComparator.filter_out_courses_that_overlap(course_to_add, courses_after_selected)

			for req in all_course_reqs:
				req_numbers[req] = req_numbers[req] - 1

			return find_schedule_recurse(courses_after_selected, req_numbers, selected_classes)

	def total_reqs_remaining(self, req_numbers):
		total = 0
		for req in req_numbers:
			total = total + req_numbers[req]

		return total

	def generator_to_list(self, generator):
		all_courses_list = []
		num = 0
		for item in generator:
			all_courses_list.append(item)

			num = num + 1

		return all_courses_list
