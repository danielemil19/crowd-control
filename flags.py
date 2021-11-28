from gpiozero import Button,Buzzer,RGBLED

# Global variables for sensors and modules
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
	