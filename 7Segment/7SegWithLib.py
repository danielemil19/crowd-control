from gpiozero import LEDCharDisplay, LEDMultiCharDisplay
from time import sleep

def number_converter(num):
    temp = list(str(num))
    temp[-1] += '.'
    return temp

c = LEDCharDisplay(4, 17, 22, 10, 9, 11, 0, dp=5, active_high=False)
d = LEDMultiCharDisplay(c, 2, 3, active_high=False)

d.value = ['2', '2.']

for x in range(99):
    d.value = number_converter(x)
    sleep(1)

sleep(20)
