from .. import Application

class NodeApplication(Application):
	def __init__(self, custom_dict={}):
		Application.__init__(self, 'node')