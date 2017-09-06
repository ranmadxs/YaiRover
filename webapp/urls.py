'''
Created on 20-08-2017

@author: esanchez
'''

from django.conf.urls import url
#from webapp.views import HomePageView
from webapp.views.main import MainController
from webapp.views.command import CommandController
from webapp.views.video import VideoController
from webapp.views.joystick import JoystickController

mainController = MainController()
commandController = CommandController()
videoController = VideoController()
joystickController = JoystickController()

urlpatterns = [    
    url(r'^$', mainController.index, name='index'),
    url(r'^api$', mainController.api, name='api'),
    url(r'^apiServo', mainController.apiServo, name='apiServo'),    
    url(r'^pipeline/pipeline.htm', mainController.pipeline, name='pipeline.htm'),
    url(r'^logs', mainController.logs, name='logs'),    
    url(r'^cmd', commandController.cmd, name='cmd'),
    url(r'^pipeline/cmd', commandController.pipelineCmd, name='pipelineCmd'),
    url(r'^js/pipeline.js', mainController.pipelineJs, name='pipeline.js'),
    url(r'^video/stream', videoController.stream, name='videoStream'),
    url(r'^video/snapshot', videoController.snapshot, name='videoSnapshot'),
    url(r'^js/joystickCmd.js', joystickController.joystickJs, name='joystickCmd.js'),
    url(r'^joystick/roverJoystick', joystickController.roverJoystick, name='roverJoystick'),
    url(r'^joystick/joystickDevice', joystickController.joystick, name='joystickDevice'),    
]

