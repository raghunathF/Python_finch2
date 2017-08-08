# Car alarm
# The finch sounds an alarm, alternating high pitch sounds and
# flashing red abd blue lights, until its nose is turned up

from time import sleep
from finch import Finch

finch = Finch()
x = 0

finch.led("#FE0000") # set the led to red

sleep(1.05)
finch.led("#0000FE") # set the led to blue

sleep(1.05)

finch.halt()
finch.close()
    
