import unittest
from penn.registrar import Registrar
import courseComparator
import pennScheduleBuilder

class TestScheduleBuilder(unittest.TestCase):

	def setUp(self):
		self.registrar = Registrar("UPENN_OD_emFc_1001364", "6kl4eonkquheuti65e32qick6l")

	def test_set_requirements(self):
		requirements = {}

		requirements['MDS'] = 1
		requirements['MWC'] = 2
		requirements['MQS'] = 1

		builder = pennScheduleBuilder.ScheduleBuilder()

		self.assertTrue(builder.set_requirements(requirements))

	def test_find_all_courses(self):

		builder = pennScheduleBuilder.ScheduleBuilder()

		courses = builder.find_all_courses("MWC")

		i = 0
		for item in courses:
			# print item['term']
			i = i + 1
			print i

		self.assertEqual(i, 102)


if __name__ == '__main__':
    unittest.main()


