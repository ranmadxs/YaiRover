#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15-08-2017

@author: esanchez
'''
import smbus
import time
from lib.logger import logger as log
from model.vo import YaiResult
from roverenum import EnumCommunicator
import serial



class YaiSerial():
    
    SERIAL_BAUD_RATE = 9600

    def sendCommand(self, strSend, port = EnumCommunicator.SerialEnum.SERIAL_TTYS1_PORT.value, baud = SERIAL_BAUD_RATE):
        log.debug(">> %s" % strSend)
        arduino = serial.Serial(port, baud)
        arduino.write(unicode(strSend))
        time.sleep(2)
        #Esto lee todas la lineas
        msg = arduino.read(arduino.inWaiting())
        log.debug("<< %s" % msg)
                
        return msg


class I2c():
    
    MAX_I2C_COMAND = 32
    MAX_I2C_CONTENT = 26
    I2C_DEV = 0
    YAI_COMMAND_TYPE_I2C = "I2C"
    
    def StringToBytes(self, val):
        retVal = []
        for c in val:
                retVal.append(ord(c))
        return retVal
    
    def buildI2Cpackage(self, command, total, part) :
        respCommand = "%s%s%s%s" % (self.YAI_COMMAND_TYPE_I2C, part, total, command);
        return respCommand

    def sendCommand(self, cmd, clientAddres = EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_MOTOR.value):        
        bus = smbus.SMBus(self.I2C_DEV)
        log.info(" >> %s" % cmd)
        totalParts = 1;
        if (len(cmd) > self.MAX_I2C_CONTENT) :
            totalParts = 2;
        cmd1 = cmd[:self.MAX_I2C_CONTENT]
        #print cmd1
        cmd1 = self.buildI2Cpackage(cmd1, totalParts, 1)
        log.debug("[p1]>>" + cmd1)
        messageInBytes = self.StringToBytes(cmd1)
        bus.write_i2c_block_data(clientAddres, 0, messageInBytes)
        
        #data_received_from_Arduino = bus.read_i2c_block_data(clientAddres, 0,32)
        #print(data_received_from_Arduino)
        time.sleep(.25)
        if (totalParts > 1) :
            cmd2 = cmd[self.MAX_I2C_CONTENT:]
            #print cmd2
            cmd2 = self.buildI2Cpackage(cmd2, totalParts, 2)
            log.debug("[p2]>>" + cmd2)
            messageInBytes = self.StringToBytes(cmd2)
            bus.write_i2c_block_data(clientAddres, 0, messageInBytes)
        
        time.sleep(0.2)        
        smsMessage = ""
        data_received_from_Arduino = bus.read_i2c_block_data(clientAddres, 0,32)
        for i in range(len(data_received_from_Arduino)):
            smsMessage += chr(data_received_from_Arduino[i])
        
        log.debug(data_received_from_Arduino) 
        msgStr = smsMessage.encode('utf-8')
        
        log.info(" << %s" % msgStr)
        
        return msgStr
