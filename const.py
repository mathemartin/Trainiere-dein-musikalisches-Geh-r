import screeninfo

class const:
	__m=screeninfo.get_monitors()
	_mwidth=__m[0].width
	_mheight=__m[0].height
	_entry_height=21
	_entry_width=300
	_label_width=300
	_2exp1div1200=2**(1/1200)
	for monitors in __m:
		_mwidth=max(_mwidth,monitors.width)
		_mheight=max(_mheight,monitors.height)	
	def _dez2amp(self,dezibel):
		amp=10**(dezibel/10)
		return amp
