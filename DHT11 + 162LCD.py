#Imports
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT

DHTPin = 11 #define the pin of DHT11


#Loop 
def loop():
    mcp.output(3,1) # turn on LCD backlight
    lcd.begin(16,2) # set number of LCD lines and columns on the LCD
    dht = DHT.DHT(DHTPin)   #create a DHT class object

    while(True):  # While loop repets everything within untill interupted  
        for i in range(0,15):            
            chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
            if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
                print("DHT11,OK!")
                break
            time.sleep(0.1)
        print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
        lcd.setCursor(0,0)  # set cursor position
        lcd.message("Temperature : %.2f \n"%(dht.temperature))
        lcd.setCursor(0,1)  # set cursor position
        lcd.message("Humidity : %.2f, \n"%(dht.humidity)) 
        time.sleep(2)

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