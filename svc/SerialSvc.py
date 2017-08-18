'''
Created on 17-08-2017

@author: esanchez
'''

import serial
import time

SERIAL_BAUD_RATE = 9600
SERIAL_DEFAULT_PORT = '/dev/ttyS0'

class YaiSerial():
    
    serialCommunicator = None
    port = SERIAL_DEFAULT_PORT
    baudRate = SERIAL_BAUD_RATE
    
    def __init__(self):
        print ("constructor")
        self.serialCommunicator = serial.Serial(self.port, self.baudRate, timeout=5)
    
    def send(self, str):
        
        self.serialCommunicator.write(str)
        time.sleep(1)
        msg = self.serialCommunicator.readline()
        return msg