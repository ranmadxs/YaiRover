#!/usr/bin/python

from lib.logger import logger as log
from svc.YaiCommunicatorSvc import I2c

log.info("Send command I2C")

yaiCommunicator = I2c()
yaiCommunicator.sendCommand("I2C,100001,1001,0,0,10002,None,None,None", I2c.CLIENT_ADDR_YAI_MOTOR)