import time
import grovepi
 
# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
ledbar = 5
 
grovepi.pinMode(ledbar,"OUTPUT")
time.sleep(1)
i = 0
 
# LED Bar methods
# grovepi.ledBar_init(pin,orientation)
# grovepi.ledBar_orientation(pin,orientation)
# grovepi.ledBar_setLevel(pin,level)
# grovepi.ledBar_setLed(pin,led,state)
# grovepi.ledBar_toggleLed(pin,led)
# grovepi.ledBar_setBits(pin,state)
# grovepi.ledBar_getBits(pin)

grovepi.ledBar_setLevel(ledbar, 1)

