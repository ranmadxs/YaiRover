# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import textwrap

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from lib.logger import logger as log

def index2(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index3(request):
    context = {'varName': 'xdddd'}
    log.info("index3")
    return render(request, 'index3.html', context)

class HomePageView(View):

    def dispatch(self, request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world22</title>
            </head>
            <body>
                <h1>Greetings to the world22</h1>
                <p>Hello, world33!</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)