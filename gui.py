from tkinter import *
from const import *
from table import *
from overtones import *
from scale import *
from rhythm import *
from settings import *
from button_bar import *
from dialog import *
from end_window import * 
class gui(const):
	def __init__(self):
		self.root=Tk()
		self.root.title('Trainiere dein musikalisches Gehör!')
		self.root.withdraw()
		self.setting_window()
		self.nr=-1
		self.richtige=0
	def setting_window(self):
		self.top=Toplevel(self.root)
		self._frame=Frame(self.top,width=self._mwidth,height=self._mheight,bg='black')	

		self.overtones_instance=overtones(self._frame,0,0)
		self.scale_instance=scale(self._frame,1,0)
		self.settings_instance=settings(self._frame,2,0)
		self.button_bar=button_bar(self._frame,0,1)
		
		self._frame.grid(column=0,row=0)
		self.top.protocol('WM_DELETE_WINDOW',self.root.destroy)	
	def dialog_window(self,variables):
		self.top.withdraw()
		self.dialog=Toplevel(self.root,bg='black')
		self.dialog.title('Bestimme die Intervalle!')
		self.dialog.protocol('WM_DELETE_WINDOW',self.close_dialog2)
		self.dialog_instance=dialog(self.dialog,variables)
	def close_dialog2(self):
		self.dialog.destroy()
		self.top.deiconify()
		self.nr=-1
		self.richtige=0
	def close_dialog(self):
		self.dialog.destroy()
		self.top.deiconify()
	def end_window(self,richtige,questions):
		self.top.withdraw()
		self.ende=Toplevel(self.root,bg='black')
		self.ende.protocol('WM_DELETE_WINDOW',self.close_ende)
		self.end_instance=end_window(self.ende,richtige,questions)
		self.nr=-1
		self.richtige=0
	def close_ende(self):
		self.ende.destroy()
		self.top.deiconify()
		
