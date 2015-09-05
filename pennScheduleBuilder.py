from penn.registrar import Registrar
import json

registrar = Registrar('UPENN_OD_emFc_1001364', '6kl4eonkquheuti65e32qick6l')

def set_requirements(reqs):
	if reqs == None or len(reqs) == 0:
		return 'Must have at least one requirement'

	total_credits = 0
	for req in reqs:
		total_credits = total_credits + reqs[req]
	
	if total_credits > 6.5:
		return 'Why the fuck are you taking more than six and a half classes, go outside'
	

def find_all_classes(reqType, course_level_above=None, course_level_below=None, starts_after=None):
	# First enter default params for all courses
	search_params = {}
	search_params['term'] = '2015C'
	search_params['status'] = 'O'
	search_params['is_cancelled'] = False
	# if course_level_above is not None:
	# 	search_params['course_level_above'] = course_level_above
	# if course_level_below is not None:
	# 	search_params['course_level_below'] = course_level_below
	if starts_after is not None:
		search_params['starts_at_or_after_hour'] = starts_after

	all_courses = registrar(search_params)

def enter_requirements(req_numbers, starts_after=None, ends_before=None, no_class_days=None, difficulty_limit=None, work_limit=None, lunch_break=None):
	self.req_classes = {}
	
	for req in req_numbers:
		self.req_classes[req] = self.findAllClasses(req, starts_after=starts_after) # FIX PARAM STUFF HERE
		self.filter_class_days(self.req_classes, no_class_days)



def filter_class_days(req_classes, no_class_days):
	for req in req_classes:
		current_classes = req_classes[req]
		for i in range(0, len(req_classes[req]) - 1):
			if self.class_meets_on_days(current_classes[i]):
				del current_classes[i]


def find_schedule(req_course_list, req_numbers, selected_classes):
	
	finished = True

	for req in req_numbers:
		if req_numbers[req] > 0:
			finished = False
			break

	if finished:
		return selected_classes

	for req in req_numbers:
		if req_numbers[req] == 0:
			continue

		valid_courses = req_course_list[req]
		if len(valid_courses) == 0:
			return False
		
		for i in range(0, len(req_course_list) - 1):
			
			course_to_add = req_course_list[req][i]
			# first check if this class in in selected classes
			if course_to_add in selected_classes:
				continue
				
			selected_classes.append(course_to_add)
			req_numbers[req] = req_numbers[req] - 1
				
			result = self.find_schedule(req_course_list, req_numbers, selected_classes)

			if not result:
				# Restore state from before
				selected_classes.pop()
				req_numbers[req] = req_numbers[req] + 1
			else:
				return selected_classes

	return False
