#!/usr/bin/python

from lib.logger import logger as log
from svc.YaiCommunicator import I2c

log.info("Send command I2C")

yaiCommunicator = I2c()
yaiCommunicator.sendCommand("I2C,100001,1001,0,0,10002,None,None,None")