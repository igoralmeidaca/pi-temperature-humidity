from grove.gpio import GPIO
 
 
class GroveLed(GPIO):
    def __init__(self, pin):
        super(GroveLed, self).__init__(pin, GPIO.OUT)
 
    def on(self):
        self.write(1)
 
    def off(self):
        self.write(0)
 
 
Grove = GroveLed
 
 
def main():
    import sys
    import time
    import psutil
 
    if len(sys.argv) < 2:
        print('Usage: {} pin'.format(sys.argv[0]))
        sys.exit(1)
 
    led = GroveLed(int(sys.argv[1]))
 
    while True:
        if psutil.cpu_percent() >= 80:
            led.on()

        time.sleep(10)
        led.off()     

 
if __name__ == '__main__':
    main()