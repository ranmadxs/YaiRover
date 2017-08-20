'''
Created on 20-08-2017

@author: esanchez
'''

from django.conf.urls import url
import webapp
from webapp.views import HomePageView

urlpatterns = [
    
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^index2.html$', webapp.views.index2, name='index2'),
    url(r'^index3.html$', webapp.views.index3, name='index3'),
    
]

