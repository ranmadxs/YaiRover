'''
Created on 17-08-2017

@author: esanchez
'''

#from svc.SerialSvc import YaiSerial
import serial

arduino = serial.Serial('/dev/ttyUSB0', 9600)
arduino.write("0YL69")

#yaiSerial = YaiSerial()
#yaiSerial.send("XDDDD")