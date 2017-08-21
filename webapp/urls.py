'''
Created on 20-08-2017

@author: esanchez
'''

from django.conf.urls import url
import webapp
from webapp.views import HomePageView

urlpatterns = [
    
    url(r'^$', webapp.views.index, name='index'),
    #url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^api$', webapp.views.api, name='api'),
    url(r'^roverJoystick', webapp.views.roverJoystick, name='roverJoystick'),
    url(r'^pipeline', webapp.views.pipeline, name='pipeline'),
    url(r'^logs', webapp.views.logs, name='logs'),
    
]

