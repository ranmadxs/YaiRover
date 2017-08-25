'''
Created on 25-08-2017

@author: instala
'''
from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic.base import View
from lib.logger import logger as log
from svc.CameraSvc import VideoCamera

class VideoController():
    
    videoCamera = VideoCamera()
    
    def genFrame(self):
        frame = self.videoCamera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')        
    
    def stream(self, request):
        return HttpResponse(self.genFrame(), content_type='multipart/x-mixed-replace; boundary=frame')