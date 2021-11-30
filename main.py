import flags
import modules
from time import sleep

#creates global variables for sensors and modules to use
flags.init()

#initializes RGBLED, buzzer, and 7Segment
modules.init()

#import buttons and PIRSensors initializes them.
#has to be called after modules init or potential crash
import buttons
import PIRSensors.PIRSensors

from BarcodeScan.scan import scan
print("Done")
modules.buzzer.beep(0.1,0,1,True)

# Whole program works with interrupts and threads
# so sleep main one infinitely
while True:
    ""
