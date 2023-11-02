class overtone_matrix:
	def __init__(self,overtones):
		self.overtones=overtones
	@property	
	def overtones(self):
		return self.__overtones
	@overtones.setter
	def overtones(self,overtones):
		self.__overtones=overtones
		self.count=len(overtones)
