import RPi.GPIO as GPIO
import dht11
import time
import datetime
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=5)

lcd_columns = 16
lcd_rows = 2

lcd_rs = DigitalInOut(board.D25)
lcd_en = DigitalInOut(board.D24)
lcd_d4 = DigitalInOut(board.D23)
lcd_d5 = DigitalInOut(board.D17)
lcd_d6 = DigitalInOut(board.D27)
lcd_d7 = DigitalInOut(board.D22)

# Initialise the LCD class
lcd = Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

try:
        while True:
            result = instance.read()
            if result.is_valid():
                temperature = "T:%-3.1fC" % result.temperature
                humidity = "  H:%-3.1f%%" % result.humidity
                lcd.message = str(datetime.datetime.now()) + "\n" + temperature + humidity

                #lcd.message = "Adafruit CharLCD\nCP Raspberry Pi"                
                #print("Last valid input: " + str(datetime.datetime.now()))
                #print(temperature)
                #print(humidity)

            time.sleep(10)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()