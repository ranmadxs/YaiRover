'''
Created on 15-08-2017

@author: esanchez
'''
from model.vo import YaiCommand
import inspect

def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            print value

yaiCommand = YaiCommand()
 
print yaiCommand.__str__()

props(yaiCommand)