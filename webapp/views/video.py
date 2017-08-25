'''
Created on 25-08-2017

@author: instala
'''
from django.shortcuts import render
from django.http import StreamingHttpResponse
#from django.views.generic.base import View
from lib.logger import logger as log
from svc.CameraSvc import VideoCamera

class VideoController():
    
    
    def genFrame(self, camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')        
    
    def stream(self, request):
        return StreamingHttpResponse(self.genFrame(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')