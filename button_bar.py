from tkinter import *
from tkinter import ttk
from const import *

class button_bar(const):
	def __init__(self,root,c,r):
		self._button1=Button(root,text='Vorhören')
		self._button2=Button(root,text='Start')
		self._button3=Button(root,text='Einstellungen speichern')
		
		self._button1.grid(column=c,row=r,sticky='we')
		self._button2.grid(column=c+1,row=r,sticky='we')
		self._button3.grid(column=c+2,row=r,sticky='we')
	def clos(self,root):
		print(1)
