from gpiozero import LEDCharDisplay, LEDMultiCharDisplay
from time import sleep

c = LEDCharDisplay(4, 17, 22, 10, 8, 11, 0, dp=5, active_high=False)
d = LEDMultiCharDisplay(c, 2, 3, active_high=False)
d.value = ('4.','3')

sleep(20)
