# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^articles/(?P<id>\d+)/$', views.detail, name='detail'),
]
