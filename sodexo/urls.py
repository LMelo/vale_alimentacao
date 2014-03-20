#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url
from sodexo import views

urlpatterns = patterns(
    '',
    url(r'^$', views.welcome, name='welcome')
)