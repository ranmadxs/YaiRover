'''
Created on 17-08-2017

@author: esanchez
'''

#from svc.SerialSvc import YaiSerial
import serial

arduino = serial.Serial('/dev/ttyS0', 9600)
arduino.write("Hola mundo desde Orange Pi Zero")
#yaiSerial = YaiSerial()
#yaiSerial.send("XDDDD")
