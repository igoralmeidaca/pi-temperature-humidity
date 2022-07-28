from __future__ import print_function
import time, sys, signal, atexit
from upm import pyupm_my9221 as upmMy9221

def main():
    # Instantiate a MY9221, we use D8 for the data, and D9 for the
    # data clock.  This was tested with a Grove LED bar.
    myLEDBar = upmMy9221.GroveLEDBar(8, 9)

    # Exit handlers
    def SIGINTHandler(signum, frame):
        raise SystemExit

    def exitHandler():
        myLEDBar.setBarLevel(0, True)
        print("Exiting")
        sys.exit(0)

    # This function lets you run code on exit
    atexit.register(exitHandler)
    # This function stops python from printing a stacktrace when you hit control-C
    signal.signal(signal.SIGINT, SIGINTHandler)

    directionBool = True
    level = 1

    x = 0
    while(1):
        # If it's less than 10
        # light up the LED now
        # call show_LED again in 50 ms
        if (level <= 10):
            myLEDBar.setBarLevel(level, directionBool)
            level += 1
        # Switch LED lighting directions between lighting cycles
        else:
            directionBool = not directionBool
            level = 1
            time.sleep(1)
        time.sleep(.05)
        x += 1

if __name__ == '__main__':
    main()