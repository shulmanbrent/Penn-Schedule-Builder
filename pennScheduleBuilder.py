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
		self.req_types[req] = self.findAllClasses(req, params) ## FIX PARAM STUFF HERE



def find_schedule(req_course_list, req_numbers, selected_classes):
	
	if len(req_numbers) == 0:
		return selected_classes

	for req in req_numbers:
		valid_courses = req_course_list[req]
		
