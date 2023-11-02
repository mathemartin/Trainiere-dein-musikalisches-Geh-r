class random_matrix:
	def __init__(self,chord_list):
		self.chord_list=chord_list
	@property
	def chord_list(self):
		return self.__chord_list
	@chord_list.setter
	def chord_list(self,chord_list):
		self.__chord_list=chord_list
		self.count=len(chord_list)
