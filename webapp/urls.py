'''
Created on 20-08-2017

@author: esanchez
'''

from django.conf.urls import url
#from webapp.views import HomePageView
from webapp.views.main import MainController
from webapp.views.command import CommandController

mainController = MainController()
commandController = CommandController()

urlpatterns = [    
    url(r'^$', mainController.index, name='index'),
    url(r'^api$', mainController.api, name='api'),
    url(r'^apiServo', mainController.apiServo, name='apiServo'),
    url(r'^roverJoystick', mainController.roverJoystick, name='roverJoystick'),
    url(r'^pipeline', mainController.pipeline, name='pipeline'),
    url(r'^logs', mainController.logs, name='logs'),
    url(r'^joystick.js', mainController.joystickJs, name='joystick.js'),
    url(r'^cmd', commandController.cmd, name='cmd'),
]

