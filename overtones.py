from table import *
from glob import *

class overtones(table):
	def __init__(self,root,c,r):
		paths=self.read_overtones()
		presets=self.clean_presets(paths)
		presets.append('Gitarrenspektrum (theoretisch)')
		super().__init__(root,'Anzahl der Obertöne: ',presets,
		c,r,'Frequenz f_n','Amplitude a_n','Phasenverschiebung')
		self._overtones=40
		count=IntVar(self._frame,value=self._overtones)
		self._rows['textvariable']=count
		self.fill_guitar()
	def fill_guitar(self):
		self._preset.set('Gitarrenspektrum (theoretisch)')
		for i in range(self._overtones):
			f_n=100*(i+1)
			phi_n=0
			if i%2==0:
				a_n=1/(i+1)**2
			else:
				a_n=0
			if i%4==2:
				phi_n=0.5
			self.create_row(f_n,a_n,phi_n)
	def handle_overtones(self,event):
		value=int(self._rows.get())
		#print(type(self._overtones.get()))
		if value!=self._overtones:
			if value>self._overtones and self._preset.get()=='Gitarrenspektrum (theoretisch)':
				for i in range(value-self._overtones):
					self.create_row(100*(self._overtones+i+1),0,0)
			elif value>self._overtones:
				for i in range(value-self._overtones):
					self.create_row(0,0,0)
			else:
				for i in range(self._overtones-value):
					self.delete_row()
			self._overtones=value
	def handle_preset(self,event):
		for i in range(self._overtones):
				self.delete_row()
		if self._preset.get()=='Gitarrenspektrum (theoretisch)':
			self.fill_guitar()
		else:
			path=self._preset.get()
			path='overtones/'+path+'.txt'
			file0=open(path,'r')
			data=file0.read()
			data=data.replace(',','.')
			data=data.split('\n')
			#overtone_list=[]
			for d in data:
				data_line=data[data.index(d)].split('\t')
				#overtone_list.append(data_line)
				if len(data_line)>=2:
					amp=self._dez2amp(float(data_line[1]))
					self.create_row(data_line[0],amp,0)
			#overtone_list.remove([''])
			self._overtones=len(data)-1
			self._rows.delete(0,END)
			self._rows.insert(0,self._overtones)
			file0.close()
			#print(overtone_list)
			
			#return overtone_list
	def clean_presets(self,paths):
		presets=[]
		for p in paths:
			p=p.replace('overtones/','')
			p=p.replace('.txt','')
			presets.append(p)
		return presets
	def read_overtones(self):
		return glob('overtones/*.txt')

