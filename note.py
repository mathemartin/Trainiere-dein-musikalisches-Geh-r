class note:
	def __init__(self,no,faktor,octave):
		self.no=no
		self.faktor=faktor
		self.octave=octave
	@property
	def octave(self):
		return self.__octave
	@octave.setter
	def octave(self,octave):
	#	if type(octave)==type(3):
	#		self.__octave=octave
		self.__octave=int(octave)
	def frequency(self,firstnote_freq):
		return firstnote_freq*self.faktor*2**self.octave
	def __eq__(self,other):
		if self.no==other.no and self.faktor==other.faktor:
			return True
		else:
			return False
	def abs_pitch(self,keyfreq=440):
		return 2**(self.octave)*self.faktor*keyfreq
	def interval(self,other,scalecount=12):
		self_=self.no+self.octave*scalecount
		other_=other.no+other.octave*scalecount
		return int(other_-self_)
