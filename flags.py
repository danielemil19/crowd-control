from gpiozero import Button,Buzzer,RGBLED

def init():
	global leftflag
	global rightflag
	global valid
	global count
	global maxcount
	global setcount
	leftflag = False
	rightflag = False
	valid = False
	setcount = False
	count = 0
	maxcount = 10
