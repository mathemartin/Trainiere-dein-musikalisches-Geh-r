from tkinter import *
from variables import *
from numpy import *

class end_window:
	def __init__(self,root,richtige,questions):
		prozent=round(floor(100*int(richtige)/int(questions)))
		if prozent<50:
			liste=['Das war nichts, du taube Nuss!','Blaß mal deine Ohren frei!','Da hört ja meine taube Oma mehr!']
			m2=choice(liste)+' Versuche eine einfachere Einstellung.'
			col='red'
		elif prozent>=50 and prozent<75:
			liste=['Hast du geraten?','Das geht besser.']
			m2=choice(liste)+' Versuche es nochmal!'
			col='yellow'
		elif prozent>=75 and prozent<88:
			m2='Das war schon ganz gut. Aber da geht nochwas!'
			col='green'
		elif prozent>=88:
			m2='Du hörst das Gras wachsen! Versuche mal eine schwierigere Einstellung.'
			col='green'
		message='Du hast '+str(richtige)+' von '+str(questions)+' Fragen richtig beantwortet.'
		message=message+'\nDas sind '+str(prozent)+'%.'
		label=Label(root,text=message,bg='black',fg='white')
		label2=Label(root,text=m2,bg='black',fg=col,font = "Verdana 10 bold")
		label.pack()
		label2.pack()
