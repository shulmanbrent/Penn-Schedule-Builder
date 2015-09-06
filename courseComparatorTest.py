import unittest
from penn.registrar import Registrar
import courseComparator

class TestCourseComparator(unittest.TestCase):

	def test_shared_meeting_days_some(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		cis262 = r.section('cis', '262', '001')
		cis380 = r.section('cis', '380', '001')
		shared_days = courseComparator.shared_meeting_days(cis262, cis380)
		self.assertEqual(len(shared_days), 2)

	def test_shared_meeting_days_none(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		cis262 = r.section('cis', '262', '001')
		cis419 = r.section('cis', '419', '401')
		shared_days = courseComparator.shared_meeting_days(cis262, cis419)
		self.assertEqual(len(shared_days), 0)

	def test_course_times_overlap_true(self):
		cis262time = (12, 13)
		cis320time = (12.3, 14)
		self.assertTrue(courseComparator.course_times_overlap(cis262time, cis320time))

	def test_course_times_overlap_false(self):
		cis262time = (12, 13)
		cis380time = (13, 14)
		self.assertFalse(courseComparator.course_times_overlap(cis262time, cis380time))

	def test_single_course_no_conflict(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		cis262 = r.section('cis', '262', '001')
		cis380 = r.section('cis', '380', '001')
		self.assertFalse(courseComparator.courses_overlap(cis262, cis380))

	def test_single_course_conflict(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		cis262 = r.section('cis', '262', '001')
		cis320 = r.section('cis', '320', '001')
		self.assertTrue(courseComparator.courses_overlap(cis262, cis320))

	def test_multiple_courses_some_conflicts(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		cis262 = r.section('cis', '262', '001')
		cis320 = r.section('cis', '320', '001')
		cis380 = r.section('cis', '380', '001')
		econ001 = r.section('econ', '001', '205')
		all_courses = [cis320, cis380, econ001]
		remaing_courses = courseComparator.filter_out_courses_that_overlap(cis262, all_courses)
		self.assertEqual(len(remaing_courses), 1)

	def test_multiple_sections_of_same_course(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		econ001001 = r.section('econ', '001', '001')
		econ001002 = r.section('econ', '001', '002')
		self.assertTrue(courseComparator.courses_overlap(econ001001, econ001002))

	def test_filter_out_courses_where_prereq_not_met(self):
		r = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")
		courses_taken = ["CIS 160", "CIS 110"]
		cis121 = r.section('cis', '121', '001')
		cis262 = r.section('cis', '262', '001')
		all_courses = [cis121, cis262]
		courses_eligble_for = courseComparator.filter_out_courses_where_prereq_not_met(all_courses, courses_taken)
		self.assertEqual(len(courses_eligble_for), 1)


if __name__ == '__main__':
    unittest.main()


