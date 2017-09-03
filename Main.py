#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 13-08-2017

@author: esanchez
'''

from lib.logger import logger as log
from svc.CameraSvc import FsWebCam


log.info('>> Inicio YaiRover <<')

log.info('tomando foto con la camara webCam')

camera = FsWebCam()
camera.capturarDatos()

log.info('foto terminada de capturar')

raise Exception("yaiCommand no puede ser nulo") 