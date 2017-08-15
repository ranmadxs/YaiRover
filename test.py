#!/usr/bin/python

import smbus
import time

LCD_ADDR = 0x09

def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

def SayHello():
        bus = smbus.SMBus(0)        
        messageInBytes = StringToBytes("I2C12SERIAL,100001,1001,0,0,1000")
        #3,None,None,None
        bus.write_i2c_block_data(LCD_ADDR, 0, messageInBytes)
        
SayHello()