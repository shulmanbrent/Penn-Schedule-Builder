import pennScheduleBuilder
import json

if __name__ == '__main__':
	builder = pennScheduleBuilder.ScheduleBuilder()

	requirements = {}

	requirements['MC1'] = 1
	# requirements['MWC'] = 1
	requirements['MDL'] = 1
	requirements['MDH'] = 1

	builder.set_requirements(requirements)


	builder.enter_preferences(starts_after="10:00")

	result = builder.find_schedule()

	print json.dumps(result, indent=4, sort_keys=True, separators=(', ', ': '))