from gpiozero import Button,Buzzer,RGBLED
from colorzero import Color


#Buttons init
buttonLeft=Button(14)
buttonRight= Button(15)
buttonSet= Button(18)
buttonCam= Button(27)

# Increases the second digit of maxcount if in set mode
def buttonpressLeft():
    import modules
    import flags
    if flags.setcount:
        flags.maxcount += 10
        if flags.maxcount > 99:
            flags.maxcount %= 10
        modules.displaynum(flags.maxcount)

# Increases the first digit of maxcount if in set mode
def buttonpressRight():
    import flags
    import modules
    if flags.setcount:
        if flags.maxcount%10 == 9:
            flags.maxcount -= 9
        else:
            flags.maxcount += 1
        
        modules.displaynum(flags.maxcount)

# Set mode to true if set button is held
# Display maxcount in 7 segment
def buttonholdSet():
    import flags
    import modules
    modules.buzzer.beep(0.1,0,1, True)
    flags.setcount = True
    modules.displaynum(flags.maxcount)

# Set mode to false if set button is pressed
# Display count in 7 segment
def buttonpressSet():
    import flags
    import modules
    if flags.setcount:
        modules.buzzer.beep(0.1,0,1, True)
        flags.setcount = False
        modules.displaynum(flags.count)
        if flags.count < flags.maxcount:
            modules.led.color = Color("red")
        else:
            modules.led.color = Color("blue")
    
# Turns on cam scanner for x seconds
# If a valid ID was given, sets valid to true
# If at max capacity or invalid ID was given, buzzer beeps
def buttonpressCam():
    from BarcodeScan.scan import scan
    from colorzero import Color
    import flags
    import modules
    if not flags.setcount:
        modules.led.color = Color("purple")
        
        if flags.count < flags.maxcount:
            flags.valid = scan(False, 30)
        else:
            flags.valid = False
        
        if not flags.valid:
            modules.buzzer.beep(0.1,0.1,3, True)
            if flags.count >= flags.maxcount:
                modules.led.color = Color("red")
            else:
                modules.led.color = Color("blue")
        if flags.valid:
            modules.buzzer.beep(0.1,0,1, True)
            modules.led.color = Color("green")


# Putting lambda functions to their interrupts
buttonLeft.when_pressed = buttonpressLeft
buttonRight.when_pressed = buttonpressRight
buttonSet.hold_time = 2
buttonSet.when_held = buttonholdSet
buttonSet.when_pressed = buttonpressSet
buttonCam.when_pressed = buttonpressCam
