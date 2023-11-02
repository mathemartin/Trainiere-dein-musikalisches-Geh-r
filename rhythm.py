from tkinter import *
from tkinter import ttk
from const import *

class rhythm(const):
	def __init__(self,root,c,r):
		columnnames=('Ton','Dauer (in Sekunden)')
		self._columnwidth=20
		self._entryheight=23
		self._scrolly=0
		self._frame=Frame(root,bg='black')
		self._tableframe=Frame(self._frame,bg='white')
		self._scrollbar=Scrollbar(self._tableframe,orient=VERTICAL)
		self._headerframe=Frame(self._frame,bg='black')
		self._tabtopframe=Frame(self._tableframe)
		self._fillframe=Frame(self._tableframe)
		self._datacanvas=Canvas(self._tableframe,height=69,width=len(columnnames)*20*8.3,
		scrollregion=(0, 0, 0, self._scrolly),yscrollcommand=self._scrollbar.set)
		self._dataframe=Frame(self._datacanvas)
		self._datacanvas.create_window((0,0),window=self._dataframe,anchor='nw')
		self._name=Label(self._headerframe,fg='white',bg='black',
		text='Anzahl der Melodietöne:   ')
		self.anzahl=2
		count=IntVar(self._frame,value=self.anzahl)
		self._rows=Entry(self._headerframe,width=2,textvariable=count)
		self._labels=[]
		self._rowlabels=[]
		self._entries=[]
		self._colnames=columnnames
		self._scrollbar['command']=self._datacanvas.yview
		max_i=len(columnnames)
		for i in range(len(columnnames)):
			self._labels.append(Label(self._tabtopframe,
			text=columnnames[i],bg='white',width=self._columnwidth))	
		self._frame.grid(column=c,row=r)
		self._headerframe.grid(column=0,row=0,sticky='w')
		self._name.grid(column=0,row=1,sticky='w')
		self._rows.grid(column=1,row=1,sticky='e')
		self._tableframe.grid(column=0,row=1,sticky='nsew')
		self._fillframe.grid(column=0,row=0)
		self._tabtopframe.grid(column=1,row=0)
		self._scrollbar.grid(column=0,row=1,sticky='ns')
		self._datacanvas.grid(column=1,row=1,sticky='nwe')
		for i in range(len(self._labels)):
			self._labels[i].grid(column=i,row=0,sticky='w')
		self._rowcount=0
		self._root=root
		self.default()
	def create_row(self,rowcontent):
		self._rowcount += 1
		v=IntVar(self._dataframe,value=rowcontent)
		row_n=Entry(self._dataframe,textvariable=v,width=self._columnwidth)
		label_n=Label(self._dataframe,text=self._rowcount,width=self._columnwidth,
		anchor='w')
		row_n.grid(column=1,row=self._rowcount)
		label_n.grid(column=0,row=self._rowcount)
			
		self._entries.append(row_n)
		self._rowlabels.append(label_n)
		self._scrolly=self._scrolly+self._entryheight
		self._datacanvas.configure(scrollregion=(0,0,0,self._scrolly))
			
	def delete_row(self):
		e=self._entries[self._rowcount-1]
		l=self._rowlabels[self._rowcount-1]
		e.destroy()
		l.destroy()
		del self._entries[self._rowcount-1]
		del self._rowlabels[self._rowcount-1]
		self._rowcount -= 1
		self._scrolly=self._scrolly-self._entryheight
		self._datacanvas.configure(scrollregion=(0,0,0,self._scrolly))
	def delete_all(self):

		for i in range(self.anzahl):
			self.delete_row()
		
	def set_count(self,count):
		self.anzahl=count
		count=IntVar(self._frame,value=self.anzahl)
		self._rows=Entry(self._headerframe,width=2,textvariable=count)
	def default(self):
		#self.delete_all()
		#self.anzahl=2
		
		for i in range(self.anzahl):
			self.create_row(1)
		#r=self._rowcount-self.anzahl
		#for i in range(r):
			#self.delete_row()

	def handle_rhythm(self):
		value=int(self._rows.get())
		if value!=self.anzahl:
			if value>self.anzahl:
				for i in range(value-self.anzahl):
					self.create_row(1)
			else:
				for i in range(self.anzahl-value):
					self.delete_row()
			self.anzahl=value

