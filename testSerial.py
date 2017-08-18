'''
Created on 17-08-2017

@author: esanchez
'''

import sys
from SerialSvc import YaiSerial
sys.path.insert(0, '../svc/SerialSvc')


import SerialSvc

yaiSerial = YaiSerial()
yaiSerial.send("XDDDD")