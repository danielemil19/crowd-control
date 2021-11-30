from gpiozero import MotionSensor

# PIR sensors init, params are for noise
pir1 = MotionSensor(23, False, queue_len=1, threshold=0.99, sample_rate=1000000)
pir2 = MotionSensor(24, False, queue_len= 1, threshold=0.99, sample_rate=1000000)

# Raises rightflag. If leftflag has already been raised,
# that means motion from left to right was detected and
# someone has exited. Decrease counter by one
def detectmotionright():
    import flags
    import modules
    from colorzero import Color
    print("left")
    
    flags.rightflag = True
    modules.led.color = Color("red")
    
    if flags.leftflag:   
        flags.count -= 1
        if flags.count < 0:
            flags.count = 0
        if not flags.setcount:
            modules.displaynum(flags.count)
        
        flags.rightflag = False
        flags.leftflag = False
        
# Raises leftflag. If rightflag has already been raised,
# that means motion from right to left was detected and
# someone has entered. Increase counter and buzz if
# valid flag is false
def detectmotionleft():
    import flags
    import modules
    from colorzero import Color
    print("right")
    
    flags.leftflag = True
    modules.led.color = Color("red")
    
    if flags.rightflag:
        if flags.valid:
            flags.valid = False
        else:
            modules.buzzer.beep(3,0,1, True)
        
        flags.count += 1
        if not flags.setcount:
            modules.displaynum(flags.count)
        flags.leftflag = False
        flags.rightflag = False

# Incase one sensor goes off but not the other, reset it's state
def stoppedmotionright():
    import flags
    import modules
    from colorzero import Color
    flags.rightflag = False
    if not flags.leftflag:
        if flags.count >= flags.maxcount:
            modules.led.color = Color("red")
        elif flags.valid:
            modules.led.color = Color("green")
        elif flags.count < flags.maxcount:
            modules.led.color = Color("blue")
def stoppedmotionleft():
    import flags
    import modules
    from colorzero import Color
    flags.leftflag = False
    if not flags.rightflag:
        if flags.count >= flags.maxcount:
            modules.led.color = Color("red")
        elif flags.valid:
            modules.led.color = Color("green")
        elif flags.count < flags.maxcount:
            modules.led.color = Color("blue") 

    
# Putting lambda functions to their interrupts
pir1.when_motion = detectmotionright
pir2.when_motion = detectmotionleft 
pir1.when_no_motion = stoppedmotionright
pir2.when_no_motion = stoppedmotionleft
