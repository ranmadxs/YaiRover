'''
Created on 22-08-2017

@author: instala
'''
from model.vo import YaiCommand

class YaiCommandSvc():
    
    def buildMessage(self, yaiCommand = None):
        if not yaiCommand is None:
            yaiCommand.message = "%s,%s,%s,%s,%s,%s,%s,%s,%s" %(yaiCommand.TIPO_CALL, yaiCommand.COMMAND, 
                                                      yaiCommand.P1, yaiCommand.P2, yaiCommand.P3, yaiCommand.P4, 
                                                      yaiCommand.P5, yaiCommand.P6, yaiCommand.P7)
        return yaiCommand
    
   # def buildCommand(self, yaiCommand = None):
        