'''
Created on 25-08-2017

@author: instala
'''
from django.shortcuts import render
from django.http import StreamingHttpResponse, HttpResponse
#from django.views.generic.base import View
from lib.logger import logger as log
from svc.CameraSvc import VideoCamera

class VideoController():
    
    def getSnapshot(self, camera):
        frame = camera.get_frame()
        #yield (b'--frame\r\n'
        #       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        return frame     
    
    def getStream(self, camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')        
    
    def snapshot(self, request):
        log.info("Snapshot Web")        
        #videoCamera = VideoCamera()
        #image_data = videoCamera.get_image()
        #return HttpResponse(image_data, content_type="image/jpg")
        return StreamingHttpResponse(self.getSnapshot(VideoCamera()), content_type="image/jpg; boundary=frame")
        
    def stream(self, request):
        return StreamingHttpResponse(self.getStream(VideoCamera()), content_type='multipart/x-mixed-replace; boundary=frame')