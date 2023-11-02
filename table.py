from tkinter import *
from tkinter import ttk
from const import *

class table(const):
	def __init__(self,root,name,presets,c,r,*columnnames):
		self._columnwidth=20
		self._entryheight=23
		self._scrolly=0
		#self._quantity=40
		self._frame=Frame(root,bg='black')
		self._tableframe=Frame(self._frame,bg='white')
		self._scrollbar=Scrollbar(self._tableframe,orient=VERTICAL)
		self._headerframe=Frame(self._frame,bg='black')
		self._tabtopframe=Frame(self._tableframe)
		self._fillframe=Frame(self._tableframe)
		self._datacanvas=Canvas(self._tableframe,width=len(columnnames)*20*8.3,
		scrollregion=(0, 0, 0, self._scrolly),yscrollcommand=self._scrollbar.set)
		self._dataframe=Frame(self._datacanvas)
		self._datacanvas.create_window((0,0),window=self._dataframe,anchor='nw')
		self._preset=ttk.Combobox(self._headerframe)
		self._preset['values']=presets
		self._presetlabel=Label(self._headerframe,fg='white',bg='black',text='Preset:')
		self._name=Label(self._headerframe,fg='white',bg='black',text=name)
		#count=IntVar(self._frame),value=self._overtones)
		self._rows=Entry(self._headerframe,width=3)
		self._labels=[]
		self._entries=[]
		self._colnames=columnnames
		self._scrollbar['command']=self._datacanvas.yview
		max_i=len(columnnames)
		for i in range(len(columnnames)):
			self._labels.append(Label(self._tabtopframe,
			text=columnnames[i],bg='white',width=self._columnwidth))	
		self._frame.grid(column=c,row=r)
		self._headerframe.grid(column=0,row=0,sticky='w')
		self._presetlabel.grid(column=0,row=0,sticky='w')
		self._preset.grid(column=1,row=0,sticky='w')
		self._name.grid(column=0,row=1,sticky='w')
		self._rows.grid(column=1,row=1,sticky='w')
		self._tableframe.grid(column=0,row=1,sticky='nsew')
		#self._fillframe.grid(column=0,row=0)
		self._tabtopframe.grid(column=1,row=0)
		self._scrollbar.grid(column=0,row=1,sticky='ns')
		self._datacanvas.grid(column=1,row=1,sticky='nwe')
		for i in range(len(self._labels)):
			self._labels[i].grid(column=i,row=0,sticky='w')
		self._rowcount=0
		self._root=root

		#self.fill_guitar()
		
		#self._datacanvas.bind('<Configure>', self.create_row)	
	def create_row(self,*rowcontent):
		if len(rowcontent)==len(self._colnames):
			row_n=[]
			self._rowcount += 1
			for i in range(len(self._colnames)):
				v=DoubleVar(self._dataframe,value=rowcontent[i])
				row_n.append(Entry(self._dataframe,textvariable=v,
				width=self._columnwidth))
				row_n[i].grid(column=i,row=self._rowcount)

			self._entries.append(row_n)
			self._scrolly=self._scrolly+self._entryheight
			self._datacanvas.configure(scrollregion=(0,0,0,self._scrolly))
		else:
			print('Fehler: Falsche Anzahl an Spalten.')
	def delete_row(self):
		e=self._entries[self._rowcount-1]
		for i in range(len(self._colnames)):
			e[i].destroy()
		del self._entries[self._rowcount-1]
		self._rowcount -= 1
		self._scrolly=self._scrolly-self._entryheight
		self._datacanvas.configure(scrollregion=(0,0,0,self._scrolly))		
	
