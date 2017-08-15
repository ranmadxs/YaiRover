#!/usr/bin/python

import smbus
import time

MAX_I2C_COMAND = 32
MAX_I2C_CONTENT = 26
LCD_ADDR = 0x09
I2C_DEV = 0
YAI_COMMAND_TYPE_I2C = "I2C"


def StringToBytes(val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal

def buildI2Cpackage(command, total, part) :
    respCommand = "%s%s%s%s" % (YAI_COMMAND_TYPE_I2C, part, total, command);
    return respCommand

def sendI2CCommand(cmd):
        bus = smbus.SMBus(I2C_DEV)
        totalParts = 1;
        if (len(cmd) > MAX_I2C_CONTENT) :
            totalParts = 2;
        cmd1 = cmd[:MAX_I2C_CONTENT]
        cmd1 = buildI2Cpackage(cmd1, totalParts, 1)
        messageInBytes = StringToBytes(cmd1)
        bus.write_i2c_block_data(LCD_ADDR, 0, messageInBytes)

        if (totalParts > 1) :
            toEnd = -1*MAX_I2C_CONTENT
            cmd2 = cmd[toEnd:]
            cmd2 = buildI2Cpackage(cmd2, totalParts, 2)
            messageInBytes = StringToBytes(cmd2)
            bus.write_i2c_block_data(LCD_ADDR, 0, messageInBytes)
        
sendI2CCommand("SERIAL,100001,1001,0,0,10003,None,None,None")