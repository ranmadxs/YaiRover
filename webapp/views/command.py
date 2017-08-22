'''
Created on 21-08-2017

@author: esanchez
'''
from lib.logger import logger as log
from django.http import HttpResponse
from model.vo import YaiCommand
from svc.YaiCmdSvc import YaiCommandSvc

class CommandController():
    
    yaiCommandSvc = YaiCommandSvc()
    
    def cmd(self, request):            
        yaiCommand = YaiCommand(request)
        yaiCommand = self.yaiCommandSvc.buildMessage(yaiCommand)
        log.debug(yaiCommand.__str__())
        #en el return debe estar el string que devuelve el servicio    
        return HttpResponse("logs")