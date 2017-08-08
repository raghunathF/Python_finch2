# A simple Finch dance in Python

from finch import Finch
from time import sleep

print("Finch's First Python program.")

# Instantiate the Finch object
snakyFinch = Finch()
    

# Do a six step dance
snakyFinch.led(254,0,0)
snakyFinch.wheels(1,1)
sleep(2)
print("second line")

snakyFinch.led(0,254,0)
snakyFinch.wheels(0,1)
sleep(2)
print("third line")

snakyFinch.led(0,0,254)
snakyFinch.wheels(1,0)
sleep(2)
print("third line")

snakyFinch.led(254,0,254)
snakyFinch.wheels(-1,-1)
sleep(2)
print("third line")

snakyFinch.led(0,254,254)
snakyFinch.wheels(0.2,-1)
sleep(2)
print("third line")

snakyFinch.led(254,254,254)
snakyFinch.wheels(0.3,0.3)
sleep(2.5)
print("third line")

snakyFinch.wheels(0,0)
snakyFinch.close();

