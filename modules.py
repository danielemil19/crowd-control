from gpiozero import Buzzer,RGBLED, LEDCharDisplay, LEDMultiCharDisplay
from colorzero import Color

# Initializes 7 segment, buzzer, and RGBLED and makes them global
def init():
    global mchardisplay
    global buzzer
    global led
    chardisplay = LEDCharDisplay(4, 17, 22, 10, 9, 11, 0, dp=5, active_high=False)
    mchardisplay = LEDMultiCharDisplay(chardisplay, 2, 3, active_high=False)
    mchardisplay.plex_delay = 0.007
    displaynum(0)
    buzzer = Buzzer(25)
    buzzer.off()
    
    led = RGBLED(19,13,6)
    led.color = Color("blue")

# Displays input number with a period to avoid bug
# INPUT: int:num -> integer to display
def displaynum(num):
    temp = list(str(num))
    temp[-1] += '.'
    mchardisplay.value = temp