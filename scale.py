from table import *
from math import *
from glob import *
import os

class scale(table):
	def __init__(self,root,c,r):
		paths=self.read_scales()
		presets=self.clean_scales(paths)
		super().__init__(root,'Anzahl der Tonleitertöne: ',
		presets,c,r,'Halbtöne','Faktor','Cent')
		self.notes=12
		count=IntVar(self._frame,value=self.notes)
		self._rows['textvariable']=count
		self.equal_temperament()
	def equal_temperament(self):
		self.notes=12
		self._rows.delete(0,END)
		self._rows.insert(0,12)
		self._preset.set('gleichstufig')
		for i in range(self.notes):
			nummer=i
			faktor=2**(i/12)
			cent=100*i
			self.create_row(nummer,faktor,cent)
	def handle_scale(self,event):
		value=int(self._rows.get())
		if value!=self.notes:
			if value>self.notes:
				for i in range(value-self.notes):
					self.create_row(self._rowcount,1,0)
			else:
				for i in range(self.notes-value):
					self.delete_row()
			self.notes=value
		
	def handle_preset(self,event):
		for i in range(self.notes):
			self.delete_row()
		if self._preset.get()=='gleichstufig':
			self.equal_temperament()
		else:
			[path,ratioflag]=self.create_path()
			file0=open(path,'r')
			data=file0.read()
			data=data.replace(',','.')
			data=data.split('\n')
			#overtone_list=[]
			for d in data:
				data_line=data[data.index(d)].split()
				#overtone_list.append(data_line)
				if len(data_line)>=2:
					if ratioflag==0:
						cent=float(data_line[1])
						ratio=self._cent2ratio(float(data_line[1]))
					else:
						ratio=self._ratio2float(data_line[1])						
						cent=self._ratio2cent(data_line[1])
					self.create_row(data_line[0],ratio,cent)
			#overtone_list.remove([''])
			self.notes=len(data)-1
			self._rows.delete(0,END)
			self._rows.insert(0,self.notes)
			file0.close()
		#elif :
		#	self.notes=12
		#	self._rows.delete(0,END)
		#	self._rows.insert(0,12)
		#besser: for p in self._presets
		#		lesen
		#		self.notes bestimmen/ändern
		#		self._rows
		#		nach _ratio unterscheiden...
		#		self.create_row(...)
	def handle_factor(self,event):
		factor=self.float2(event.widget.get())
		cent=round(log(factor,self._2exp1div1200))
		cent_entry=event.widget.target
		cent_entry.delete(0,END)
		cent_entry.insert(0,cent)
	def handle_cent(self,event):
		cent=float(event.widget.get())
		factor=2**(cent/1200)
		factor_entry=event.widget.target
		factor_entry.delete(0,END)
		factor_entry.insert(0,factor)
	def create_row(self,*rowcontent):
		super().create_row(*rowcontent)
		entr=self._entries[-1]
		entr[1].target=entr[2]
		entr[2].target=entr[1]
		entr[1].bind('<FocusOut>',self.handle_factor)
		entr[2].bind('<FocusOut>',self.handle_cent)
		
		#print(self._entries[len(self._entries)-1][2].get())
	def float2(self,equation):
    		if '/' in equation:
        		y = equation.split('/')
        		x = float(y[0])/float(y[1])
    		else:
        		x=float(equation)
    		return x
	def create_path(self):
		preset=self._preset.get()
		path='scale/'+preset+'.txt'
		if os.path.isfile(path):
			return [path, 0]
		else:
			path='scale/'+preset+'_ratio.txt'
			return [path, 1]
	def clean_scales(self,paths):
		presets=[]
		for p in paths:
			p=p.replace('scale/','')
			p=p.replace('.txt','')
			p=p.replace('_ratio','')
			presets.append(p)
		return presets
	def read_scales(self):
		return glob('scale/*.txt')	
	def _cent2ratio(self,cent):
		ratio=2**(cent/1200)
		return ratio
	def _ratio2cent(self,ratio):
		ratio=self._ratio2float(ratio)
		cent=round(1200*log(ratio)/log(2))
		return cent
	def _ratio2float(self,ratio):
		ratio=ratio.split('/')
		if len(ratio)>1:
			ratio=int(ratio[0])/int(ratio[1])
		else:
			ratio=int(ratio[0])
		return float(ratio)
