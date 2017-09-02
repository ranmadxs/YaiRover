#!/usr/bin/python

from lib.logger import logger as log
from svc.YaiCommunicatorSvc import I2c
from roverenum import EnumCommunicator

log.info("Send command I2C")

yaiCommunicator = I2c()
#yaiCommunicator.sendCommand("I2C,100001,1001,0,0,10002,None,None,None", EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_MOTOR.value)
yaiCommunicator.sendCommand("I2C,200003,2001,0,20003,None,None,None,None", EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_SERVO.value)