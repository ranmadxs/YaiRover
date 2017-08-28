'''
Created on 17-08-2017

@author: esanchez
'''

from svc.YaiCommunicatorSvc import YaiSerial
import serial

#arduino = serial.Serial('/dev/ttyS1', 9600)
#arduino.write("Hola mundo desde Orange Pi Zero")
yaiSerial = YaiSerial()
resp = yaiSerial.sendCommand("SERIAL,100001,1001,0,0,10002,None,None,None")
print(resp)
