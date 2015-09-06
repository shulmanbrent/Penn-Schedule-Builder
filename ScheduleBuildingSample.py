import pennScheduleBuilder

if __name__ == '__main__':
	builder = pennScheduleBuilder()

	requirements = {}

	requirements['MC1'] = 1
	requirements['MWC'] = 1
	requirements['MDL'] = 1
	requirements['MDH'] = 1

	builder.set_requirements(requirements)

	b