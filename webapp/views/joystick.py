'''
Created on 03-09-2017

@author: esanchez
'''

from django.shortcuts import render
from django.http import HttpResponse
from lib.logger import logger as log
from svc.ContextSvc import YaiContext

class JoystickController():

    yaiContext = YaiContext()

    def joystick(self, request):
        log.info("joystick page")
        context = self.yaiContext.getCommonContext()
        return render(request, 'pages/joystick/joystick.htm', context)

    def roverJoystick(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("roverJoystick page")
        return render(request, 'pages/joystick/old_joystick.htm', context)

    def joystickJs(self, request):
        context = self.yaiContext.getCommonContext()
        log.info("roverJoystick js")
        return render(request, 'js/joystick.js', context)       