# Car alarm
# The finch sounds an alarm, alternating high pitch sounds and
# flashing red abd blue lights, until its nose is turned up

from time import sleep
from finch import Finch
from msvcrt import getch

finch = Finch()

def main():

	#while(1):
	key = 0
	ultrasound_value = 0

	while(1) :

		ultrasound_value = finch.new_obstacle()
		if(ultrasound_value > 2000) :
			finch.wheels(0.5,0.5)
		else :
			finch.wheels(0,0.5)
			sleep(0.1)
		#print (ultrasound_value
		#key = ord(getch())


	finch.halt()
	finch.close()

if __name__ == '__main__':
	
	main()
