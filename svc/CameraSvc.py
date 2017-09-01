'''
Created on 22-03-2016

@author: esanchez
'''

from time import localtime, strftime
import os
from lib.logger import logger as log
import cv2

FOLDER_WEBCAM = '/tmp/motion/'
CAMERA_DEVICE = 0

PIC_WIDTH = 384
PIC_HEIGHT = 288

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(CAMERA_DEVICE)
        log.info("Init VideoCamera")
        #log.info(self.video.CV_CAP_PROP_BRIGHTNESS)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_image(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

class FsWebCam():
    def capturarDatos(self):        
        devCamera = "/dev/video%s"%CAMERA_DEVICE
        if not os.path.exists(FOLDER_WEBCAM):
            os.makedirs(FOLDER_WEBCAM)
        print "Usando camara %s ..." % devCamera
        fileTime = strftime("%Y-%m-%d_%H:%M:%S", localtime())
        #log.info(fileTime)
        fileName = '%spic_%s.jpg'%(FOLDER_WEBCAM, fileTime)    
        #log.info(fileName)
        commandCamera = 'fswebcam -d %s -r %dx%d %s -S2 --set brightness=65' % (devCamera, PIC_WIDTH, PIC_HEIGHT, fileName)
        log.debug(commandCamera)
        os.system(commandCamera)  
        
