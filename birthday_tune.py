# Car alarm
# The finch sounds an alarm, alternating high pitch sounds and
# flashing red abd blue lights, until its nose is turned up

from time import sleep
from finch import Finch

finch = Finch()


# finch.led("#550000") # set the led to red
# finch.finch_2_buzzer(3,880,60)
# sleep(1.00)
# finch.led("#005500") # set the led to blue
# finch.finch_2_buzzer(3,493,60)
# sleep(1.00)

# finch.led("#000055") # set the led to red
# finch.finch_2_buzzer(3,523,60)
# sleep(1.00)
# finch.led("#550055") # set the led to blue
# finch.finch_2_buzzer(3,587,60)
# sleep(1.00)

# finch.led("#555500") # set the led to red
# finch.finch_2_buzzer(3,659,60)
# sleep(1.00)
# finch.led("#005555") # set the led to blue
# finch.finch_2_buzzer(3,698,60)
# sleep(1.00)

# finch.finch_2_buzzer(3,880,60)
# sleep(1.00)
# finch.led("#005500") # set the led to blue
# finch.finch_2_buzzer(3,493,60)
# sleep(1.00)

# finch.led("#000055") # set the led to red
# finch.finch_2_buzzer(3,523,60)
# sleep(1.00)
# finch.led("#550055") # set the led to blue
# finch.finch_2_buzzer(3,587,60)
# sleep(1.00)

# finch.led("#555500") # set the led to red
# finch.finch_2_buzzer(3,659,60)
# sleep(1.00)
# finch.led("#005555") # set the led to blue
# finch.finch_2_buzzer(3,698,60)
# sleep(1.00)


A = []
B = []
C = []
D = []
E = []
F = []


notes	= [262,262,294,262, 349, 330, 262, 262, 294, 262, 392, 349, 262, 262, 523, 440, 349, 330, 294, 466, 466, 440,349, 392, 349];
time	= [4, 4, 8, 8, 8, 10, 4, 4, 8, 8, 8, 10, 4, 4, 8, 8, 8, 8, 8, 4, 4, 8, 8, 8, 12];

def song(frequency , duration ):
	finch.finch_2_buzzer(3,frequency*4,40)
	sleep(duration*0.1)
	

def main():
	for i in range(0,len(notes)):
		song(notes[i],time[i]);

	finch.halt()
	finch.close()

if __name__ == '__main__':
	
	main()