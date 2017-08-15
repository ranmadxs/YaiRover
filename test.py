#!/usr/bin/python

from lib.logger import logger as log
from svc.YaiCommunicator import I2c

log.info("Send command I2C")

yaiCommunicator = I2c()
yaiCommunicator.sendCommand("SERIAL,100001,1001,0,0,10003,None,None,None")