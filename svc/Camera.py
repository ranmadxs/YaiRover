'''
Created on 22-03-2016

@author: esanchez
'''

from time import localtime, strftime
import os

FOLDER_WEBCAM = '/tmp/motion/'
CAMERA_DEVICE = '/dev/video0'
PIC_WIDTH = 384
PIC_HEIGHT = 288

class WebCam():
    def capturarDatos(self):        
        
        if not os.path.exists(FOLDER_WEBCAM):
            os.makedirs(FOLDER_WEBCAM)
        print "Usando camara %s ..." % CAMERA_DEVICE
        fileTime = strftime("%Y-%m-%d_%H:%M:%S", localtime())
        fileName = '%spic_%s.jpg'%(FOLDER_WEBCAM, fileTime)    
        os.system('fswebcam -d %s -r %dx%d %s -S2 --set brightness=65%' % (CAMERA_DEVICE, PIC_WIDTH, PIC_HEIGHT, fileName))  
        
