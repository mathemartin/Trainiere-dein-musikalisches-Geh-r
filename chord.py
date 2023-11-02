class chord:
	def __init__(self,notes_list):
		self.chord=notes_list
	@property
	def chord(self):
		return self.__chord
	@chord.setter
	def chord(self,notes_list):
		self.__chord=notes_list
		self.count=len(self.__chord)
	def add(self,note):
		self.__chord.append(note)
		self.count=len(self.__chord)
	def delete(self,note):
		self.__chord.remove(note)
