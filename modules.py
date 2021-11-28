from gpiozero import Buzzer,RGBLED, LEDCharDisplay, LEDMultiCharDisplay
from colorzero import Color

def init():
    global mchardisplay
    global buzzer
    global led
    chardisplay = LEDCharDisplay(4, 17, 22, 10, 9, 11, 0, dp=5, active_high=False)
    mchardisplay = LEDMultiCharDisplay(chardisplay, 2, 3, active_high=False)
    mchardisplay.plex_delay = 0.007
    buzzer = Buzzer(25)
    buzzer.off()
    
    led = RGBLED(19,13,6)
    led.color = Color("blue")
    
def displaynum(num):
    temp = list(str(num))
    temp[-1] += '.'
    mchardisplay.value = temp