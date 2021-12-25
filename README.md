# Tom-LCD



Two modules are used in the code, PCF8574.py and Adafruit_LCD1602.py
PCF8574.py is used to provide I2C communication mode and operation method of some of the ports for the 
RPi and PCF8574 IC Chip. Adafruit module Adafruit_LCD1602.py is used to provide some functional operation 
method for the LCD1602 Display.
In the code, first get the object used to  operate the PCF8574’s port, then get the object used to operate the  operate the PCF8574’s port, then get the object used to operate the 
LCD1602

Module PCF8574
This module provides two classes PCF8574_I2C and PCF8574_GPIO.
Class PCF8574_I2C：provides reading and writing method for PCF8574.
Class PCF8574_GPIO：provides a standardized set of GPIO functions.
More information can be viewed through opening PCF8574.py.
Adafruit_LCD1602 Module

Module Adafruit_LCD1602
This module provides the basic operation method of LCD1602, including class Adafruit_CharLCD. Some 
member functions are described as follows:
def begin(self, cols, lines): set the number of lines and columns of the screen.
def clear(self): clear the screen
def setCursor(self, col, row): set the cursor position
def message(self, text): display contents
More information can be viewed through opening Adafruit_CharLCD.py