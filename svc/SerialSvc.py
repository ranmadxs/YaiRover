# -*- coding: utf-8 -*-

'''
Created on 17-08-2017

@author: esanchez
'''

import serial
import time

SERIAL_BAUD_RATE = 9600
SERIAL_DEFAULT_PORT = '/dev/ttyUSB0'

class YaiSerial():
    
    serialCommunicator = None
    port = SERIAL_DEFAULT_PORT
    baudRate = SERIAL_BAUD_RATE
    
    def __init__(self):
        self.serialCommunicator = serial.Serial(self.port, self.baudRate, timeout=5)
    
    def send(self, str):
        
        self.serialCommunicator.write(str)
        time.sleep(1)
        msg = self.serialCommunicator.readline()
        return msg