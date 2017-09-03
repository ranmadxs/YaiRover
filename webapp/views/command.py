#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21-08-2017

@author: esanchez
'''
from lib.logger import logger as log
from django.http import HttpResponse
from model.vo import YaiCommand
from svc.YaiCmdSvc import YaiCommandSvc
from django.shortcuts import render
from roverenum import EnumCommons

class CommandController():
    
    yaiCommandSvc = YaiCommandSvc()
    
    def pipelineCmd(self, request):
        log.info("pipelineCmd")
        log.info(request.POST["csrfmiddlewaretoken"])
        #log.info(request.POST)
        listCmds = []
        countTotal = 0;
        for postElement in request.POST.lists():
            if not postElement[0] == "csrfmiddlewaretoken":
                yaiCommand = YaiCommand()
                yaiCommand.__resToObject__(postElement[1])
                if((yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_SERIAL.value) 
                   or (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_I2C.value)):
                    yaiCommand.execute = True                
                    self.yaiCommandSvc.execute(yaiCommand)
                    countTotal = countTotal + 1
                log.debug( yaiCommand)
                
        
        return HttpResponse("total Execute Commands :: %d" % countTotal )
    
    def cmd(self, request):            
        yaiCommand = YaiCommand(request)
        yaiCommand.type = yaiCommand.TIPO_CALL
        yaiCommand = self.yaiCommandSvc.buildMessage(yaiCommand)        
        log.debug(yaiCommand.__str__())
        yaiResponse = self.yaiCommandSvc.execute(yaiCommand)
        #en el return debe estar el string que devuelve el servicio    
        return HttpResponse(yaiResponse.__str__())