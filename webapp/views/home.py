#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 03-09-2017

@author: esanchez
'''

from django.shortcuts import render
from django.http import HttpResponse
from lib.logger import logger as log
from svc.ContextSvc import YaiContext
from roverenum.EnumCommunicator import JoystickEnum

class HomeController():

    yaiContext = YaiContext()
    
    def index(self, request):
        log.info("Index page Home controller")
        
        context = self.yaiContext.getCommonContext()
        urlBase =request.get_host()
        
        context["HOST_NAME"] = urlBase.split(':', 1)[0]
        log.info(context["HOST_NAME"])
        return render(request, 'pages/home/home.htm', context)


