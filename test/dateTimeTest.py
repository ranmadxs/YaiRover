'''
Created on 25-08-2017

@author: instala
'''

import time
import datetime

today = datetime.datetime.now().strftime('%d/%m/%Y %H:%M %p')

now = datetime.datetime.now()


print "%s/%s/%s %s:%s" %( now.day, now.month, now.year, now.hour, now.minute)

print today