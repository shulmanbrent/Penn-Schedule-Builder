from penn.registrar import Registrar
import json

registrar = Registrar('UPENN_OD_emFc_1001364', '6kl4eonkquheuti65e32qick6l')

def set_requirements(reqs):
	if reqs === None or len(reqs) === 0:
		return 'Must have at least one requirement'
	
	## ADD REAL ERROR HANDLING
	

def find_all_classes(reqType, course_level_above=None, course_level_below=None, starts_after=None, starts_on_day=None):
	search_params = {}
	search_params['term'] = '2015C'
	search_params[]
	if course_level_above is not None:
		search_params['course_level_above'] = course_level_above
	if course_level_below is not None:
		search_params['course_level_below'] = course_level_below
	if starts_after is not None:
		search_params['starts_at_or_after_hour'] = starts_after
	if starts_on_day is not None:
		search_params['starts_on_day'] = starts_on_day

	all_courses = registrar(search_params)

def enter_requirements(req_numbers, otherParams):
	self.req_types = {}
	
	for req in req_numbers:
		self.req_types[req] = self.findAllClasses(req, params) # FIX PARAM STUFF HERE



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

