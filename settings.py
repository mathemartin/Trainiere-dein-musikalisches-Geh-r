from tkinter import *
from tkinter import ttk
from const import *
from rhythm import *

class settings(const):
	def __init__(self,root,c,r):
		presets=('Standard')
		test_type=('Melodie','Harmonie','Melodie und Harmonie')
		keynote=('fester Grundton','variabler Grundton')
		up_down=('aufsteigend', 'absteigend', 'auf- und absteigend')
		self.__style=ttk.Style()
		self.__style.configure('TCheckbutton',foreground='white',background='black',
		indicatorcolor='white')
		self.__style.map('TCheckbutton',
                background=[('pressed', 'black'),
                            ('focus', 'black')])
		self._frame=Frame(root,bg='black')
		self._subframe=Frame(self._frame,bg='black')
		self._subframe2=Frame(self._frame,bg='black')
		self._preset=ttk.Combobox(self._frame)
		self._test_type=ttk.Combobox(self._frame)
		self._keynote=ttk.Combobox(self._frame)
		self._up_down=ttk.Combobox(self._frame)
		self._preset['values']=presets
		self._test_type['values']=test_type
		self._keynote['values']=keynote
		self._up_down['values']=up_down
		self._preset_label=Label(self._frame,fg='white',bg='black',text='Preset: ')
		self._test_type_label=Label(self._frame,fg='white',bg='black',text='Art des Tests: ')
		self._keynote_label=Label(self._frame,fg='white',bg='black',text='Grundton: ')
		self._up_down_label=Label(self._frame,fg='white',bg='black',text='Melodieverlauf: ')
		self._questions_label=Label(self._frame,fg='white',bg='black',
		text='Anzahl der Fragen: ')
		self._harmonycount_label=Label(self._frame,fg='white',bg='black',
		text='Anzahl der Hamonietöne: ')
		self._freq_range_label1=Label(self._subframe2,fg='white',bg='black',
		text='Frequenzbereich: von ')
		self._freq_range_label2=Label(self._subframe2,fg='white',bg='black',
		text='Hz bis ')
		self._freq_range_label3=Label(self._subframe2,fg='white',bg='black',
		text='Hz')
		self._intervals_label=Label(self._frame,fg='white',bg='black',
		text='zu testende Intervalle (durch Komma getrennt): ')
		self._questions=Entry(self._frame,width=3)
		self._harmonycount=Entry(self._frame,width=2)
		self._freq_range_from=Entry(self._subframe2,width=5)
		self._freq_range_to=Entry(self._subframe2,width=5)
		self._intervals=Entry(self._frame,width=30)
		
		self._random_rhythm=ttk.Checkbutton(self._subframe,text='zufälliger Rhythmus',
		style='TCheckbutton')
		#print(self._random_rhythm.winfo_class())
		
		
		self._frame.grid(column=c,row=r)
		self._preset_label.grid(column=0,row=0,sticky='w')
		self._preset.grid(column=1,row=0,sticky='w')
		self._test_type_label.grid(column=0,row=1,sticky='w')
		self._test_type.grid(column=1,row=1,sticky='w')
		self._keynote_label.grid(column=0,row=2,sticky='w')
		self._keynote.grid(column=1,row=2,sticky='w')
		self._up_down_label.grid(column=0,row=3,sticky='w')
		self._up_down.grid(column=1,row=3,sticky='w')	
		self._questions_label.grid(column=0,row=4,sticky='w')	
		self._questions.grid(column=1,row=4,sticky='w')
		self._subframe.grid(column=0,row=5,columnspan=2,sticky='w')
		self._random_rhythm.grid(column=0,row=0,sticky='w')	
		self.rhythm_instance=rhythm(self._subframe,0,1)
		self._harmonycount_label.grid(column=0,row=6,sticky='w')
		self._harmonycount.grid(column=1,row=6,sticky='w')
		self._subframe2.grid(column=0,row=7,columnspan=2,sticky='w')
		self._freq_range_label1.grid(column=0,row=0,sticky='w')
		self._freq_range_from.grid(column=1,row=0,sticky='w')
		self._freq_range_label2.grid(column=2,row=0,sticky='w')
		self._freq_range_to.grid(column=3,row=0,sticky='w')
		self._freq_range_label3.grid(column=4,row=0,sticky='w')
		self._intervals_label.grid(column=0,row=8,sticky='w',columnspan=2)
		self._intervals.grid(column=0,row=9,sticky='w',columnspan=2)
		self.default_settings()
		
	def default_settings(self):
		self._test_type.set('Melodie')
		self._keynote.set('variabler Grundton')
		self._up_down.set('auf- und absteigend')
		questions=IntVar(self._frame,value=25)
		harmonycount=IntVar(self._frame,value=1)
		freq_range_from=IntVar(self._subframe2,value=100)
		freq_range_to=IntVar(self._subframe2,value=1000)
		intervals=StringVar(self._frame,value='0,1,2,3,4,5,6,7,8,9,10,11,12')
		self._questions['textvariable']=questions
		self._harmonycount['textvariable']=harmonycount
		self._freq_range_from['textvariable']=freq_range_from
		self._freq_range_to['textvariable']=freq_range_to
		self._intervals['textvariable']=intervals
		self._random_rhythm['variable']=0
		self._preset.set('Standard')
		
		
		
	def handle_preset(self,event):
		if self._preset.get()=='Standard':
			self.default_settings()
		
