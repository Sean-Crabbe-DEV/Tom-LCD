# Messages
# Defines the messages to be sent
message1 = 'Hello'
message2 = ''

#Imports
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime

#Loop 
def loop():
    mcp.output(3,1) # turn on LCD backlight
    lcd.begin(16,2) # set number of LCD lines and columns on the LCD

    lcd.setCursor(16,0)  # set cursor position
    lcd.message(message1)
    sleep(5)
    lcd.clear()
    lcd.setCursor(15,0)  # set cursor position
    lcd.message(message1)
    sleep(5)
    lcd.clear()
    lcd.setCursor(14,0)  # set cursor position
    lcd.message(message1)
    sleep(5)
    lcd.clear()
    lcd.setCursor(13,0)  # set cursor position
    lcd.message(message1)
    sleep(5)
    lcd.clear()
"""  
    while(True):  # While loop repets everything within untill interupted        
        #lcd.clear() # Cleears the LCD
        lcd.setCursor(0,0)  # set cursor position
        lcd.message(message1)     
        sleep(1) # Waits or Sleeps for 1 second 
"""

# Destroy (Clears LCD)     
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp) # Defines GPIO Pins

#Main
if __name__ == '__main__':
    print ('Program is starting ... ') # Prints ('Program is starting ... ' into the shell/IDE
    try:
        loop() # Calls loop
    except KeyboardInterrupt:
        destroy() # Calls destroy if keboard inturupt is used

