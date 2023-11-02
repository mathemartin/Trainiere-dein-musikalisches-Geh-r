from gui import *
from math import *
from variables import *
g=gui()
nr=-1
richtige=0
static=0
def handle_keypress(event):
	if event.keysym=='Return':
		g.overtones_instance.handle_overtones(event)
		g.scale_instance.handle_scale(event)
		g.settings_instance.rhythm_instance.handle_rhythm()
def handle_combobox(event):
	if event.widget==g.settings_instance._preset:
		g.settings_instance.handle_preset(event)
	elif event.widget==g.scale_instance._preset:
		g.scale_instance.handle_preset(event)
	elif event.widget==g.overtones_instance._preset:
		g.overtones_instance.handle_preset(event)
	elif event.widget==g.settings_instance.rhythm_instance._rows:
		g.settings_instance.rhythm_instance.handle_rhythm()
def save(event):
	g.settings_instance.rhythm_instance.handle_rhythm()


def handle_start(event):
	global g
	global nr
	global richtige
	global static
	g.settings_instance.rhythm_instance.handle_rhythm()
	v=variables(g,static)

	if g.nr==-1:
		static=v.firstnote
		g.nr=v.questions
		g.dialog_window(v)
	elif g.nr==0:
		g.close_dialog()
#		print(g.richtige)
#		print(v.questions)
		g.end_window(g.richtige,v.questions)
		g.nr=-1
		g.richtige=0
	else:
		g.close_dialog()
		g.dialog_window(v)
	
#	print(v.freq_matrix)
	def handle_again(event):
		#global v
		v.play_all()
		#v.play(v.freq_range_from,1)
		#v.play(v.current[0],1)
	def handle_next(event):
		global nr
		global richtige
		v.melodysub(g)
		v.harmonysub(g)
		if v.melodysub==v.melodysolution and v.harmonysub==v.harmonysolution:
			g.dialog_instance.print_correct()
			g.richtige+=1
		else:
			g.dialog_instance.print_wrong(v)

	#		v.print_solution()
		g.dialog_instance.button2.destroy()
		g.dialog_instance.button3.grid(column=2,row=1,sticky='w',columnspan=3)
		g.nr-=1
	#		g.dialog_instance.button2['text']='weiter'
			#weiter=True
	#	v.print_solution()
	try:
		g.dialog_instance.button1.bind('<Button-1>',handle_again)
		g.dialog_instance.button2.bind('<Button-1>',handle_next)
		g.dialog_instance.button3.bind('<Button-1>',handle_start)
	except:
		pass
def handle_hear(event):
	global g
	global static
	g.settings_instance.rhythm_instance.handle_rhythm()
	v=variables(g,static)
	v.play(440,2)
g.top.bind('<Key>',handle_keypress)
g.top.bind('<<ComboboxSelected>>',handle_combobox)
#g.scale_instance._preset.bind('<FocusOut>',handle_widget)
g.button_bar._button1.bind('<Button-1>',handle_hear)
g.button_bar._button2.bind('<Button-1>',handle_start)
g.button_bar._button3.bind('<Button-1>',save)
g.top.mainloop()

