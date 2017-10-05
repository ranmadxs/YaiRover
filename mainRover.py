'''
Created on 13-09-2017

@author: instala
'''

import os
import threading


def runCamera():
    os.system("python CameraController.py")

def runRover():
    os.system("python manage.py runserver 0.0.0.0:8000")

threadCamera = threading.Thread(target=runCamera, name='threadCamera')
threadCamera.start()

threadRover = threading.Thread(target=runRover, name='threadRover')
threadRover.start()
