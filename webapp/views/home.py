#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 03-09-2017

@author: esanchez
'''

from django.shortcuts import render
from django.http import HttpResponse
from lib.logger import logger as log
from svc.ContextSvc import YaiContext

class HomeController():

    yaiContext = YaiContext()
    
    def index(self, request):
        log.info("Index page Home controller")
        return render(request, 'pages/home/iframe.htm')


