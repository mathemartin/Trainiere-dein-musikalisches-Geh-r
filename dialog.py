from tkinter import *
from variables import *
from numpy import *

class dialog:
	def __init__(self,root,variables):
		#self.__frame=Frame(root,fg='white',bg='black')
		self.__singular=(not variables.harmonybool and variables.melodycount==2) or (not variables.melodybool and variables.harmonycount==2)
		if not 'gleichstufig' in variables.scale_txt and not 'mikrotonal' in variables.scale_txt:
			self.__tonstufe='\nTonstufe: '+str(int(variables.random_matrix[0][0].no))#das geht so nicht
		else:
			self.__tonstufe=''
		if self.__singular:
			self.__question=Label(root,fg='white',bg='black',
			text='Welches Intervall hörst du?'+self.__tonstufe)
		else:
			self.__question=Label(root,fg='white',bg='black',
			text='Welche Intervalle hörst du?'+self.__tonstufe)
		self.__canvas1=Canvas(root,bg='black',width=80,height=100,highlightthickness=0)
		self.__canvas2=Canvas(root,bg='black',width=100,height=35,highlightthickness=0)
		self.__canvas1.create_line(70,0,70,100,arrow='first',fill='white')
		self.__canvas2.create_line(0,10,100,10,arrow='last',fill='white')
		self.__canvas1.create_text(8,0,text='Tonhöhe',fill='white',anchor='nw')
		self.__canvas2.create_text(60,15,text='Zeit',fill='white',anchor='nw')
		self.button1=Button(root,text='nochmal hören')
		self.button2=Button(root,text='Eingabe bestätigen')
		self.button3=Button(root,text='weiter')
	
		self.__rowmax=2*variables.harmonycount+3
		self.__colmax=max(2*variables.melodycount-1,3)
		self.button1.grid(column=1,row=1,sticky='w')
		self.button2.grid(column=2,row=1,sticky='w',columnspan=3)
		self.__question.grid(column=1,row=0,columnspan=self.__colmax-1)
		self.__canvas1.grid(row=self.__rowmax-4,column=0,rowspan=3,sticky='sw')
		self.__canvas2.grid(row=self.__rowmax-1,column=1,
		columnspan=min(self.__colmax-1,3),sticky='sw')
		self.harmonyentries=[]
		self.melodyentries=[]
		if variables.harmonybool and variables.melodybool:
			self.__akkordlabels=[]
			self.__tonlabels=[]
			self.harmonyentries=[]
			self.melodyentries=[]
			for i in range(variables.melodycount):
				entry=Entry(root,width=3)
				label=Label(root,text='Akkord '+str(i+1)+'   ',bg='black',fg='white')
				if i<variables.melodycount-1:
					self.melodyentries.append(entry)
					self.melodyentries[i].grid(column=2*i+2,row=self.__rowmax-2)
				self.__akkordlabels.append(label)
				self.__akkordlabels[i].grid(column=2*i+1,row=2)
				self.__tonlabels.append([])
				self.harmonyentries.append([])
				for j in range(variables.harmonycount):
					label=Label(root,
					text='Ton '+str(j+1),bg='black',fg='white')
					self.__tonlabels[i].append(label)
					self.__tonlabels[i][j].grid(column=2*i+1,
					row=self.__rowmax-2*j-2)
					if j<variables.harmonycount-1:
						entry=Entry(root,width=3)
						self.harmonyentries[i].append(entry)
						self.harmonyentries[i][j].grid(row=self.__rowmax-3-2*j, column=2*i+1)
		elif variables.melodybool:
			self.__tonlabels=[]
			self.melodyentries=[]
			for i in range(variables.melodycount):
				label=Label(root,text='   Ton '+str(i+1)+'   ',bg='black',fg='white')
				self.__tonlabels.append(label)
				self.__tonlabels[i].grid(column=2*i+1,row=self.__rowmax-2)
				if i<variables.melodycount-1:
					entry=Entry(root,width=3)
					self.melodyentries.append(entry)
					self.melodyentries[i].grid(column=2*i+2,row=self.__rowmax-2)
		elif variables.harmonybool:
			self.__tonlabels=[]
			self.harmonyentries=[]
			for i in range(variables.harmonycount):
				label=Label(root,text='Ton '+str(i+1),bg='black',fg='white')
				self.__tonlabels.append(label)
				self.__tonlabels[i].grid(column=1,row=self.__rowmax-2-2*i)
				if i<variables.harmonycount-1:
					entry=Entry(root,width=3)
					self.harmonyentries.append(entry)
					self.harmonyentries[i].grid(column=1,
					row=self.__rowmax-3-2*i)
		variables.play_all()
	def print_correct(self):
		self.__question['text']='Richtig'
		self.__question['fg']='green'
		for entry in self.melodyentries:
			self.green(entry)
		for entry in self.harmonyentries:
			try:
				self.green(entry)
			except:
				for subentry in entry:
					self.green(subentry)
	def print_wrong(self,variables):
		self.__question['text']='Falsch'
		self.__question['fg']='red'
		for i in range(len(variables.melodysolution)):
			if variables.melodysolution[i]==variables.melodysub[i]:
				self.green(self.melodyentries[i])
			else:
				self.melodyentries[i].delete(0,'end')
				self.melodyentries[i].insert(0,variables.melodysolution[i])
				self.red(self.melodyentries[i])
		for i in range(len(variables.harmonysolution)):
			try:
				for j in range(len(variables.harmonysolution[i])):
					if variables.harmonysolution[i][j]==variables.harmonysub[i][j]:
						self.green(self.harmonyentries[i][j])
					else:
						self.harmonyentries[i][j].delete(0,'end')
						self.harmonyentries[i][j].insert(0,variables.harmonysolution[i][j])
						self.red(self.harmonyentries[i][j])
			except:
				if variables.harmonysolution[i]==variables.harmonysub[i]:
					self.green(self.harmonyentries[i])
				else:
					self.harmonyentries[i].delete(0,'end')
					self.harmonyentries[i].insert(0,variables.harmonysolution[i])
					self.red(self.harmonyentries[i])
	def red(self,entry):
		entry['fg']='red'
	def green(self,entry):
		entry['fg']='green'
		
