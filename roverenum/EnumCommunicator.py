'''
Created on 23-08-2017

@author: esanchez
'''

from enum import Enum

class I2CEnum(Enum):
    I2C_CLIENT_YAI_SERVO = 8;
    I2C_CLIENT_YAI_MOTOR = 9;

class SerialEnum(Enum):
    SERIAL_TTYS0_PORT = '/dev/ttyS0'
    SERIAL_TTYS1_PORT = '/dev/ttyS1'
    SERIAL_TTYS2_PORT = '/dev/ttyS2'    