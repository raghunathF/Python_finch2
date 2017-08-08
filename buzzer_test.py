# Car alarm
# The finch sounds an alarm, alternating high pitch sounds and
# flashing red abd blue lights, until its nose is turned up

from time import sleep
from finch import Finch

finch = Finch()

finch.led("#550000") # set the led to red
finch.finch_2_buzzer(3,880,60)
sleep(1.00)
finch.led("#005500") # set the led to blue
finch.finch_2_buzzer(3,493,60)
sleep(1.00)

finch.led("#000055") # set the led to red
finch.finch_2_buzzer(3,523,60)
sleep(1.00)
finch.led("#550055") # set the led to blue
finch.finch_2_buzzer(3,587,60)
sleep(1.00)

finch.led("#555500") # set the led to red
finch.finch_2_buzzer(3,659,60)
sleep(1.00)
finch.led("#005555") # set the led to blue
finch.finch_2_buzzer(3,698,60)
sleep(1.00)

finch.finch_2_buzzer(3,880,60)
sleep(1.00)
finch.led("#005500") # set the led to blue
finch.finch_2_buzzer(3,493,60)
sleep(1.00)

finch.led("#000055") # set the led to red
finch.finch_2_buzzer(3,523,60)
sleep(1.00)
finch.led("#550055") # set the led to blue
finch.finch_2_buzzer(3,587,60)
sleep(1.00)

finch.led("#555500") # set the led to red
finch.finch_2_buzzer(3,659,60)
sleep(1.00)
finch.led("#005555") # set the led to blue
finch.finch_2_buzzer(3,698,60)
sleep(1.00)



finch.halt()
finch.close()
    
