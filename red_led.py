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
    from datetime import datetime, timedelta
    import psutil
 
    if len(sys.argv) < 2:
        print('Usage: {} pin'.format(sys.argv[0]))
        sys.exit(1)
 
    led = GroveLed(int(sys.argv[1]))
 
    lastTimeHighCpuUsage = datetime.now()
    lastHighCpuUsage
    while True:
        cpuUsage = psutil.cpu_percent()
        print("\n Last valid read: " + str(datetime.now()))
        print("CPU usage: " + str(cpuUsage))

        if cpuUsage >= 80:
            lastTimeHighCpuUsage = datetime.now()
            lastHighCpuUsage = cpuUsage
            led.on()

        if lastTimeHighCpuUsage + timedelta(minutes=30) < datetime.now():
            led.off()  

        print("Last valid max: " + str(lastTimeHighCpuUsage))
        print("Max CPU usage: " + str(lastHighCpuUsage))        

        time.sleep(10)           

 
if __name__ == '__main__':
    main()