'''
Created on 21-08-2017

@author: esanchez
'''
from lib.logger import logger as log
from django.http import HttpResponse

class CommandController():
    
    def cmd(self, request):
        log.info("cmd?TIPO_CALL=" + request.GET['TIPO_CALL'] + '&COMMAND=' + request.GET['COMMAND'])
        #en el return debe estar el string que devuelve el servicio    
        return HttpResponse("logs")