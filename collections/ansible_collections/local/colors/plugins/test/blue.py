# Ansible Custom blue test plugin definition

def is_blue(string):
	blue_values = [
	'blue',
	'#000ff',
	'#00f',
	'rgb(0,0,255)'
	]

	return string in blue_values

class TestModule(object):
	''' Test '''
	def tests(self):
		return {
			'blue': is_blue,
		}