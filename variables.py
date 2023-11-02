from numpy import *
from sounddevice import *
from random import *
import note
from random_matrix import *
from chord import *
from overtone_matrix import *
import overtone as ov
#import matplotlib.pyplot as plt
class variables:
	def __init__(self,gui,static):
		self.__maxiter=200
		self.__iter=0
		self.__fadetime=0.1
		self.static=static
		#string mit Preset für Tonskala z.B.: 'gleichstufig'
		self.scale_txt=str(gui.scale_instance._preset.get())
		#Liste der Obertöne. Die Obertöne werden als overtone-Objekt abgespeichert.
		self.__overtone_matrix=self.__read_overtones(gui)
		#Anzahl der Töne der Tonskala
		self.__notes=int(gui.scale_instance.notes)
		#Alle möglichen Töne werden aus der Tabelle eingelesen und als chord-Objekt unter self.__scale abgespeichert.
		#Das chord-Objekt besteht im Wesentlichen aus einer Liste von note-Objekten, 
		#welche die Zeilen der Tabelle mit der Tonskala enthält
		self.__scale=self.__read_scale(gui)
		#Die Art des Test wird eingelesen (z.B. 'Melodie') und in zwei boolschen Variablen gespeichert.
		test_type=gui.settings_instance._test_type.get()
		self.__melodybool=bool(test_type=='Melodie' or test_type=='Melodie und Harmonie')
		self.__harmonybool=bool(test_type=='Harmonie' or test_type=='Melodie und Harmonie')
		#Es wird als boolsche Variable eingelesen, ob der Grundton beim Test variieren soll.
		self.__static_keynote=bool(gui.settings_instance._keynote.get()=='fester Grundton')
		#Es wird eingelesen ob aufsteigende/absteigende Melodien erlaubt sind und in zwei boolschen Variablen gespeichert.
		up_down=gui.settings_instance._up_down.get()
		self.__ascending=bool(up_down=='aufsteigend' or up_down=='auf- und absteigend')
		self.__descending=bool(up_down=='absteigend' or up_down=='auf- und absteigend')
		#Anzahl der Fragen, die gestellt werden sollen
		self.questions=int(gui.settings_instance._questions.get())	
		#Anzahl der Töne in einem Akkord
		self.harmonycount=int(gui.settings_instance._harmonycount.get())
		#Niedrigste erlaubte Frequenz
		self.__freq_range_from=float(gui.settings_instance._freq_range_from.get())
		#höchste erlaubte Frequenz
		self.__freq_range_to=float(gui.settings_instance._freq_range_to.get())	
		if self.__freq_range_to/self.__freq_range_from<pow(2,1/12):
			self.__freq_range_to=self.__freq_range_from*pow(2,1/12)
		#Anzahl der Töne/Akkorde in der Melodie, wenn verneint wurde, dass es sich um einen Melodie/Harmonietest handelt,
		#wird jeweils die Anzahl der Töne der Melodie/Harmonie gleich 1 gesetzt.
		self.melodycount=int(gui.settings_instance.rhythm_instance._rows.get())
		if not self.melodybool:
			self.melodycount=1
		if not self.harmonybool:
			self.harmonycount=1
		if not self.melodybool and not self.harmonybool:
			self.melodycount=2
			self.__melodybool=True
		
		self.__random_rhythm=gui.settings_instance._random_rhythm.instate(['selected'])
		#die Länge der Töne/Akkorde in Sekunden wird eingelesen.
		self.__rhythm_vector=[]
		for i in range(self.melodycount):
			if self.__random_rhythm:
				t=choice([2,3,4,5,6,7,8])
				t=t/4
				self.__rhythm_vector.append(float(t))
			else:
				t=float(gui.settings_instance.rhythm_instance._entries[i].get())
				if t<2*self.__fadetime+0.1:
					t=2*self.__fadetime+0.1
				self.__rhythm_vector.append(t)
		self.__rhythm_cutter()
		self.__get_intervals(gui)
		#print(self.intervals)
		self.__create_firstnote()
		self.create_random_matrix()
		self.__harmonysolution()
		self.__melodysolution()
	def __rhythm_cutter(self):
		while sum(self.__rhythm_vector)>10:
			r=[]
			for t in self.__rhythm_vector:
				r.append(0.8*t)
			self.__rhythm_vector=r

	@property
	def melodybool(self):
		return self.__melodybool
	@property 
	def harmonybool(self):
		return self.__harmonybool
	def __get_intervals(self,gui):
		self.intervals=gui.settings_instance._intervals.get()
		self.intervals=self.intervals.split(',')
		for i in range(len(self.intervals)):
			self.intervals[i]=int(self.intervals[i])
		faktors=[]
		for i in self.intervals:
			for note in self.__scale.chord:
				if note.no==i and note.faktor>self.__freq_range_to/self.__freq_range_from:
					self.intervals.remove(i)#Intervalle, die zwangsläufig außerhalb der freq_range liegen, werden aussortiert.
	def play(self,frequency,time):
		default.samplerate = 44100
		
		samples = arange(time*44100) / 44100
		#wave =  32767 * np.sin(2 * np.pi * frequency * samples)
		#wav_wave = np.array(wave, dtype=np.int16)
		#sd.play(wav_wave, blocking=True)
		wave=0*samples
		for overt in self.__overtone_matrix:
			f=overt.frequency*frequency/self.__overtone_matrix[0].frequency
			wave=wave+overt.amp*sin(2*pi*f*(samples-2*pi*overt.phi))
		wave=10000*wave/max(wave)
		wave=self.__smooth(samples,time,wave,self.__fadetime,32767)
		wav_wave = array(wave, dtype=int16)
		play(wav_wave, blocking=True)
	def __smooth(self,samples,time,wave,fadeouttime,resolution):
		if 2*fadeouttime>time:
			return wave
		else:
			a=1/fadeouttime*log(1/resolution)
			t_diff=time-fadeouttime
			fadeout=minimum(1,exp(a*(samples-t_diff)))
			fadein=minimum(1,exp(-a*samples))#Bitte Formel überprüfen!!!
			return (wave*fadeout)*fadein
	def __play_harmony(self,frequencies,time):
		default.samplerate = 44100
		
		samples = arange(time*44100) / 44100
		wave=0*samples
		for frequency in frequencies:
			for row in self.__overtone_matrix:
				wave=wave+row.amp*sin(2 * pi * row.frequency*frequency/self.__overtone_matrix[0].frequency * (samples-2*pi*row.phi))
		wave=10000*wave/max(wave)
		wave=self.__smooth(samples,time,wave,self.__fadetime,32767)
		wav_wave = array(wave, dtype=int16)
		play(wav_wave, blocking=True)	
	#	plt.plot(wav_wave)
	def play_all(self):
		self.__create_freq_matrix()
		for i in range(self.melodycount):
			 self.__play_harmony(self.__freq_matrix[i],self.__rhythm_vector[i])
	#	plt.show()
	def __create_firstnote(self):
		if type(self.static)==type(0) or not self.__static_keynote:
			self.firstnote=choice(self.__scale.chord) #[choice(self.__scale.chord),0]
		else:
			self.firstnote=self.static
		if self.scale_txt=='indisch':
			self.firstnote=self.__scale.chord[0]
		#print(self.firstnote)
	def __create_firstnote_freq(self):
		if self.scale_txt in ['mitteltönig','pythagoraeisch','gleichstufig','rein','mikrotonal','wohltemperiert (Werckmeister III)']:
			faktor=self.__find_a()
			self.__firstnote_freq=220/faktor
		elif self.scale_txt=='indisch':
			self.__firstnote_freq=128
			if self.__freq_range_to<2*self.__freq_range_from:
				self.__freq_range_to=2*self.__freq_range_from
		else:
			faktor=2**(2/3)
			self.__firstnote_freq=220/faktor	
	#	if self.__firstnote_freq<self.__freq_range_from or self.__firstnote_freq>self.__freq_range_to and self.scale_txt!='indisch':
	#		self.__create_firstnote()
	#		self.__create_firstnote_freq()
	def __find_a(self):
		for note in self.__scale.chord:
			if note.no==8:
				return note.faktor

	def __random_note(self,previous_note,harm):
		interval=choice(self.intervals)
		if not harm:
			if self.__ascending and self.__descending:
				signum=choice([-1,1])		
			elif self.__ascending:
				signum=1
			elif self.__descending:
				signum=-1
		else:
			signum=1
		interval=signum*interval
		#Durch die __eq__ Methode in der Klasse note, werden zwei Objekte, die sich nur in der
		#Oktave unterscheiden als identisch interpretiert. Dadurch kann die index-Methode verwendet
		#werden.
		i=self.__scale.chord.index(previous_note)#self.__scale.chord gibt Liste der Noten-Objekte wieder.
		scale_notes=len(self.__scale.chord)
		octaves=floor((i+interval)/scale_notes)+previous_note.octave#previous_note[1]
		random_note=self.__scale.chord[mod(i+interval,scale_notes)]#AUWEIA
		#es wird ein weiteres Objekt mit fast gleichen Attributen erzeugt. es darf nicht dasselbe Objekt 
		#verwendet werden, da sonst das jeweilige Objekt in self.__scale verändert wird.
		random_note=note.note(random_note.no,random_note.faktor,octaves)
		#print([random_note,octaves])
		#print(scale_notes)

		return random_note
	def __max_matrix(self,matrix):
		lol=[]
		for r in matrix:
			lol.append(max(r))
		return max(lol)
	def __min_matrix(self,matrix):
		lol=[]
		for r in matrix:
			lol.append(min(r))
		return min(lol)
	def __reset(self):
		self.__iter+=1
		#print(self.__iter)
		if self.__iter<self.__maxiter or self.__iter>self.__maxiter*2 or (self.__iter>self.__maxiter and self.__iter<self.__maxiter*2): 
			if not self.__static_keynote:
				self.create_random_matrix()
				self.__create_freq_matrix()
				#print('neu')
				self.__harmonysolution()
				self.__melodysolution()
			else:
				#self.__create_firstnote()
				self.create_random_matrix()
				self.__create_freq_matrix()
				#print('neu')
				self.__harmonysolution()
				self.__melodysolution()
		elif self.__iter==self.__maxiter:
			self.__freq_range_to=max(self.__freq_range_to,self.__freq_range_from*2)
			print('Warnung: eingestellte Maximalfrequenz auf',self.__freq_range_to,'erhöht')
			self.create_random_matrix()
			self.__create_freq_matrix()
			self.__harmonysolution()
			self.__melodysolution()
		elif self.__iter==self.__maxiter*2:
			self.__freq_range_to=max(self.__freq_range_to,self.__freq_range_from*4)
			print('Warnung: eingestellte Maximalfrequenz auf',self.__freq_range_to,'erhöht')
			self.create_random_matrix()
			self.__create_freq_matrix()
			self.__harmonysolution()
			self.__melodysolution()
	def __multiply_matrix(self,matrix,faktor):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				matrix[i][j]=matrix[i][j]*faktor
		return matrix
	def __create_freq_matrix(self):#Fehler bei festem Grundton und vielen Aufrufen von __reset()
		#self.random_matrix()
		self.__create_firstnote_freq()
		self.__freq_matrix=[]
		for akkord in self.__random_matrix:
			akk=[]
			for n in akkord:
				oktave=n.octave
				faktor=n.faktor
				akk.append(self.__firstnote_freq*faktor*2**oktave)
			self.__freq_matrix.append(akk)	
		maxF=self.__max_matrix(self.__freq_matrix)
		minF=self.__min_matrix(self.__freq_matrix)
		fmax=self.__freq_range_to
		fmin=self.__freq_range_from
	#	print('Anfang:')
	#	print(maxF)
	#	print(minF)
		if (maxF>fmax and minF<=fmin) or (maxF>=fmax and minF<fmin):
			self.__reset()
		elif maxF>fmax and minF>=fmin:
	#		print('zu groß')
			while minF>fmin*2:
				#print(minF)
				self.__freq_matrix=self.__multiply_matrix(self.__freq_matrix,1/2)
			#	for i in range(len(self.__freq_matrix)):
			#		for j in range(len(self.__freq_matrix[0])):
			#			self.__freq_matrix[i][j]=self.__freq_matrix[i][j]/2
				maxF=self.__max_matrix(self.__freq_matrix)
				minF=self.__min_matrix(self.__freq_matrix)
	#			print('-----')
	#			print(maxF)
	#			print(minF)
			if maxF>=fmax:
				self.__reset()
		elif minF<fmin and maxF<=fmax:
	#		print('zu klein')
			while maxF<fmax/2:
				#print(maxF)
				self.__freq_matrix=self.__multiply_matrix(self.__freq_matrix,2)

			#	for i in range(len(self.__freq_matrix)):
			#		for j in range(len(self.__freq_matrix[0])):
			#			self.__freq_matrix[i][j]=self.__freq_matrix[i][j]*2
				maxF=self.__max_matrix(self.__freq_matrix)
				minF=self.__min_matrix(self.__freq_matrix)
	#			print('-----')
	#			print(maxF)
	#			print(minF)
				#F=F*2
				#minF=...
				#maxF=...
			if minF<fmin:
				self.__reset()
	@property
	def freq_matrix(self):
		return self.__freq_matrix
	def create_random_matrix(self):
		random_matrix=[]
		for i in range(self.melodycount):
			random_matrix.append([])
			for j in range(self.harmonycount):
				if i==0 and j==0:
					self.__create_firstnote()
					random_matrix[i].append(self.firstnote)
				elif i!=0 and j==0:
					random_matrix[i].append(self.__random_note(random_matrix[i-1][0],False))# !!! -1 zu 0 geändert !!!
				else:
					random_matrix[i].append(self.__random_note(random_matrix[i][j-1],True))
		#print(random_matrix)
		self.__random_matrix=random_matrix
#	def solution_matrix(self): #in Arbeit: solution-Matrix soll erwartete Eingabe enthalten. Die Eingabe soll in eine Matrix eingelesen werden, die mit der solutionmatrix identisch sein muss.
	@property
	def random_matrix(self):
		return self.__random_matrix
	def melodysub(self,gui):
		melodyentries=gui.dialog_instance.melodyentries
		melodysub=[]
		for entry in melodyentries:
			try:
				melodysub.append(int(entry.get()))
			except:
				melodysub.append(0)
		self.melodysub=melodysub
	def harmonysub(self,gui):
		harmonyentries=gui.dialog_instance.harmonyentries
		harmonysub=[]
		if self.harmonybool and self.melodybool:
			for i in range(len(harmonyentries)):
				try:	
					harmonysub.append([])
					for entry in harmonyentries[i]:
						try:
							harmonysub[i].append(int(entry.get()))
						except:
							harmonysub[i].append(0)
				except:
					try:
						harmonysub.append(int(entry.get()))
					except:
						harmonysub.append(0)
		else:
			for entry in harmonyentries:
				try:
					harmonysub.append(int(entry.get()))
				except:
					harmonysub.append(0)
		self.harmonysub=harmonysub
	def __melodysolution(self):
		scale_notes=len(self.__scale.chord)
		melodysolution=[]
		for i in range(self.melodycount-1):
			melodysolution.append(self.__random_matrix[i][0].interval(self.__random_matrix[i+1][0],scale_notes))
		if not self.melodybool:
			melodysolution=[]
		self.melodysolution=melodysolution
	def __harmonysolution(self):
		scale_notes=len(self.__scale.chord)
		harmonysolution=[]
		for i in range(self.melodycount):
			harmonysolution.append([])
			for j in range(self.harmonycount-1):
				harmonysolution[i].append(self.__random_matrix[i][j].interval(self.__random_matrix[i][j+1],scale_notes))
		if not self.harmonybool:
			harmonysolution=[]
		if not self.melodybool:
			harmonysolution=harmonysolution[0]
		self.harmonysolution=harmonysolution
	def print_solution(self):
		print('melodysolution')
		print(self.melodysolution)
		print('harmonysolution')
		print(self.harmonysolution)
		print('melodysub')
		print(self.melodysub)
		print('harmonysub')
		print(self.harmonysub)
	def __read_overtones(self,gui):
		self.__overtones=int(gui.overtones_instance._rows.get())
		overtone_matrix=[]
		for i in range(self.__overtones):
			no=i
			frequency=gui.overtones_instance._entries[i][0]
			amp=gui.overtones_instance._entries[i][1]
			phi=gui.overtones_instance._entries[i][2]
			frequency=float(frequency.get())
			phi=float(phi.get())*2*pi
			amp=float(amp.get())
			overtone=ov.overtone(no,frequency,amp,phi)
			overtone_matrix.append(overtone)
		return overtone_matrix
	def __read_scale(self,gui):
		scale=[]
		for i in range(self.__notes):
			entr=gui.scale_instance._entries[i][0]
			no=float(entr.get())
			entr=gui.scale_instance._entries[i][1]
			faktor=float(entr.get())
			octave=0
			note1=note.note(no,faktor,octave)
			scale.append(note1)
		return chord(scale)
