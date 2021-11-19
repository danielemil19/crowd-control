from RPIO import PWM
from time import sleep

PWM.setup()
PWM.init_channel(0)

# Dictionary of codes of each number to display for common cathode 7Seg
# Order of ports: dp G F E D C B A
number = {
    0: (1,1,0,0,0,0,0,0),
    1: (1,1,1,1,1,0,0,1),
    2: (1,0,2,0,0,2,0,0),
    3: (1,0,1,1,0,0,0,0),
    4: (1,0,0,1,1,0,0,1),
    5: (1,0,0,1,0,0,1,0),
    6: (1,0,0,0,0,0,1,0),
    7: (1,1,1,1,1,0,0,0),
    8: (1,0,0,0,0,0,0,0),
    9: (1,0,0,1,1,0,0,0)
}

# Dictionary for GPIO Pin Configuration; Order: dp G F E D C B A
GPIO = {
    0: 5,
    1: 0,
    2: 11,
    3: 9,
    4: 10,
    5: 22,
    6: 17,
    7: 4
}

# Pulse off and on (minimum of 4 = 40us for stable off state)
pulse = {
    0: 4,
    1: 999
}

# Adding pulse: RPIO function - add_channel_pulse(dma_channel, gpio, start, width)
PWM.add_channel_pulse(0, 2, 0, 999)
PWM.add_channel_pulse(0, 2, 1000, 999)

def set_number(number):
    # Splitting number into digits
    digits = [int(x) for x in str(number)]

    # Setting pulses for segments dp G F E D C B A for both digits
    for i in range(8):
        PWM.add_channel_pulse(0, GPIO[i], 0, pulse[number[digits[0][i]]])
        PWM.add_channel_pulse(0, GPIO[i], 1000, pulse[number[digits[1][i]]])

set_number(15)
sleep(20)

# Clearing all pulses
PWM.clear_channel(0)

# Stop all PWM activity
PWM.cleanup()