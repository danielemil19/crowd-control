from gpiozero import LEDCharDisplay, LEDMultiCharDisplay
from time import sleep

c = LEDCharDisplay(4, 17, 22, 10, 9, 11, 0, dp=5, active_high=False)
d = LEDMultiCharDisplay(c, 2, 3, active_high=False)

def number_converter(num):
    global d
    temp = list(str(num))
    temp[-1] += '.'
    d.value = temp
    
number_converter(25)