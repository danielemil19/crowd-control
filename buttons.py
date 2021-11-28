from gpiozero import Button,Buzzer,RGBLED
from colorzero import Color


#Buttons
buttonUp=Button(14)
buttonDw= Button(15)
buttonSet= Button(18)
buttonCam= Button(27)

def buttonpressUp():
    import modules
    import flags
    if flags.setcount:
        flags.maxcount += 10
        if flags.maxcount > 99:
            flags.maxcount %= 10
        modules.displaynum(flags.maxcount)

def buttonpressDw():
    import flags
    import modules
    if flags.setcount:
        if flags.maxcount%10 == 9:
            flags.maxcount -= 9
        else:
            flags.maxcount += 1
        
        modules.displaynum(flags.maxcount)

def buttonholdSet():
    import flags
    import modules
    modules.buzzer.beep(0.1,0,1, True)
    flags.setcount = True
    modules.displaynum(flags.maxcount)

def buttonpressSet():
    import flags
    import modules
    if flags.setcounter:
        modules.buzzer.beep(0.1,0,1, True)
        flags.setcount = False
        modules.displaynum(flags.count)
    

def buttonpressCam():
    from BarcodeScan.scan import scan
    from colorzero import Color
    import flags
    import modules
    
    modules.led.color = Color("purple")
    
    if flags.count < flags.maxcount:
        flags.valid = scan(True)
    else:
        flags.valid = False
    
    if not flags.valid:
        modules.buzzer.beep(0.1,0.1,3, True)
    if flags.valid:
        modules.buzzer.beep(0.1,0,1, True)
        modules.led.color = Color("green")



buttonUp.when_pressed = buttonpressUp
buttonDw.when_pressed = buttonpressDw
buttonSet.hold_time = 1
buttonSet.when_held = buttonholdSet
buttonSet.when_pressed = buttonpressSet
buttonCam.when_pressed = buttonpressCam

#Buzzer