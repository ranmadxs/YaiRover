#!/usr/bin/python

import smbus
import time

LCD_ADDR = 0x28

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

def SayHello():
        bus = smbus.SMBus(0)
        messageInBytes = StringToBytes("Hello World")
        bus.write_i2c_block_data(LCD_ADDR, 0, messageInBytes)
        
SayHello()