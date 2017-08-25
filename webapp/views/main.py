'''
Created on 21-08-2017

@author: esanchez
'''

#from roverenum import EnumCommons
from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic.base import View
from lib.logger import logger as log
from svc.ContextSvc import YaiContext

class MainController():
    
    yaiContext = YaiContext()
    
    def index(self, request):
        log.info("Index page")
        return render(request, 'index.htm')

    def api(self, request):
        log.info("Api page")
        return render(request, 'api.htm')

    def apiServo(self, request):
        log.info("ServoApi page")
        return render(request, 'apiServo.htm')

    def roverJoystick(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("roverJoystick page")
        return render(request, 'pages/joystick.htm', context)

    def joystickJs(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("roverJoystick js")
        return render(request, 'js/joystick.js', context)        

    def pipelineJs(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("pipeline js")
        return render(request, 'js/pipeline.js', context)        
            
    def logs(self, request):
        return HttpResponse("logs")
    
    def pipeline(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("pipeline")
        return render(request, 'pages/pipeline.htm', context)