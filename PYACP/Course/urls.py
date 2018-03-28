#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias
from django.conf.urls import url
from views import course_choice

urlpatterns = [
    url(r'^course_choice', course_choice, name='course_choice'),
]
