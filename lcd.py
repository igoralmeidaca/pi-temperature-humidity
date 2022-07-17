from time import sleep
import board
from digitalio import DigitalInOut
from adafruit_character_lcd.character_lcd import Character_LCD_Mono

# Modify this if you have a different sized character LCD
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
# display text on LCD display \n = new line
lcd.message = "Adafruit CharLCD\nCP Raspberry Pi"
sleep(3)
# scroll text off display
for x in range(0, 16):
    lcd.move_right()
    sleep(.2)
sleep(2)
# scroll text on display
for x in range(0, 16):
    lcd.move_left()
    sleep(.2)

