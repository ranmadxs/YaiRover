'''
Created on 22-03-2016

@author: esanchez
'''

'''
http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-set

0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
3. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
4. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
5. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
6. CV_CAP_PROP_FPS Frame rate.
7. CV_CAP_PROP_FOURCC 4-character code of codec.
8. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
9. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
10. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
11. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
12. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
13. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
14. CV_CAP_PROP_HUE Hue of the image (only for cameras).
15. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
16. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
17. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
18. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
19. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)

'''

from time import localtime, strftime
import os
from lib.logger import logger as log
import cv2
import numpy as np
import socket
import sys
import pickle

FOLDER_WEBCAM = '/tmp/motion/'
CAMERA_DEVICE = 0

PIC_WIDTH = 384
PIC_HEIGHT = 288

class VideoCameraClient():
    def __init__(self):
        self.video = cv2.VideoCapture(CAMERA_DEVICE)
        clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientsocket.connect(('localhost',8089))        
    
    def get_frame(self):
        success, image = self.video.read()
        data = pickle.dumps(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(CAMERA_DEVICE)
        log.info("Init VideoCamera")
        self.video.set(3,320)
        self.video.set(4,240)
        self.video.set(11,60)
        
        #log.info(self.video.CV_CAP_PROP_BRIGHTNESS)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the mainRover.py.
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
        
