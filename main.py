import flags
import modules
flags.init()
modules.init()

import buttons
import PIRSensors.PIRSensors
from BarcodeScan.scan import scan
print("Done")


while True:
    ""