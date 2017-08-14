'''
Created on 13-08-2017

@author: esanchez
'''

from lib.logger import logger as log
from svc.Camera import WebCam


log.info('>> Inicio YaiRover <<')

log.info('tomando foto con la camara webCam')

camera = WebCam()
camera.capturarDatos()

log.info('foto terminada de capturar')