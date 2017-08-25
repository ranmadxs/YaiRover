'''
Created on 21-08-2017

@author: esanchez
'''
from lib.logger import logger as log
from django.http import HttpResponse
from model.vo import YaiCommand
from svc.YaiCmdSvc import YaiCommandSvc
from django.shortcuts import render

class CommandController():
    
    yaiCommandSvc = YaiCommandSvc()
    
    def pipelineCmd(self, request):
        log.info("pipelineCmd")
        return HttpResponse("pipelin cmd")
    
    def cmd(self, request):            
        yaiCommand = YaiCommand(request)
        yaiCommand.type = yaiCommand.TIPO_CALL
        yaiCommand = self.yaiCommandSvc.buildMessage(yaiCommand)        
        log.debug(yaiCommand.__str__())
        yaiResponse = self.yaiCommandSvc.execute(yaiCommand)
        #en el return debe estar el string que devuelve el servicio    
        return HttpResponse(yaiResponse.__str__())