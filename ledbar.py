import time
import grovepi
 
# Connect the Grove LED Bar to digital port D5
# DI,DCKI,VCC,GND
ledbar = 5

unused = 0

# pinMode() command format header
pMode_cmd = [5]

# Set level
ledBarLevel_cmd = [52]
 
pinMode(ledbar,"OUTPUT")
time.sleep(1)
i = 0

ledBar_setLevel(ledbar, 1)

# Grove LED Bar - set level
# level: (0-10)
def ledBar_setLevel(pin, level):
	grovepi.write_i2c_block(ledBarLevel_cmd + [pin, level, unused])
	grovepi.read_i2c_block(no_bytes = 1)
	return 1

# Setting Up Pin mode on Arduino
def pinMode(pin, mode):
	if mode == "OUTPUT":
		grovepi.write_i2c_block(pMode_cmd + [pin, 1, unused])
	elif mode == "INPUT":
		grovepi.write_i2c_block(pMode_cmd + [pin, 0, unused])
	grovepi.read_i2c_block(no_bytes = 1)
	return 1