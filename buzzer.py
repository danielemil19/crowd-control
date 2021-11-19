from gpiozero import Button,Buzzer,RGBLED
from colorzero import Color

count=0
maxCount=0

def buttonpressUp():
    global count
    count+=1
    print(count)

def buttonpressDw():
    global count
    count-=1
    print(count)

def buttonpressSet():
    global count
    maxCount= count
    print(maxCount)

def buttonpressCam():
    #Camara init

#Buttons
buttonUp=Button(14)
buttonDw= Button(15)
buttonSet= Button(18)
buttonCam= Button()

buttonUp.when_pressed = buttonpressUp
buttonDw.when_pressed = buttonpressDw
buttonSet.when_pressed = buttonpressSet
buttonCam.when_pressed = buttonpressCam #to be determined

#Buzzer
bz=Buzzer(25)
bz.off()
if(count>maxCount):
    bz.on()
#RGB
led= RGBLED(19,13,6)
led.color=(1,0,0)#red,green,Blue
