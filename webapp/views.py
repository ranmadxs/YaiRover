# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import textwrap

from roverenum import EnumCommons
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from lib.logger import logger as log

def index(request):
    log.info("Index page")
    return render(request, 'index.htm')

def api(request):
    log.info("Api page")
    return render(request, 'api.htm')

def apiServo(request):
    log.info("ServoApi page")
    return render(request, 'apiServo.htm')

#Todo : Llevar a comonContext
def roverJoystick(request):
    context = {'ROVER_STOP': EnumCommons.CommandsEnum.ROVER_STOP.value, 
               'ROVER_MOVE_MANUAL_BODY' : EnumCommons.CommandsEnum.ROVER_MOVE_MANUAL_BODY.value, 
               'LASER_ACTION' : EnumCommons.CommandsEnum.LASER_ACTION.value,
               'SERVO_TYPE_SG90' : EnumCommons.ServoTypeEnum.SERVO_TYPE_SG90.value,
                }
    log.info("index3")
    return render(request, 'pages/yoistick.htm', context)

def logs(request):
    return HttpResponse("logs")

def pipeline(request):
    return HttpResponse("pipeline")

def index3(request):
    context = {'varName': 'xdddd'}
    log.info("index3")
    return render(request, 'index3.html', context)

class HomePageView(View):

    def dispatch(self, request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world22</title>
            </head>
            <body>
                <h1>Greetings to the world22</h1>
                <p>Hello, world33!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)