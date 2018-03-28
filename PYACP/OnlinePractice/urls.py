#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias

'''
功能：在线练习的路由
创建时间：2017.10.26
最后修改时间：2017.10.26
'''

from django.conf.urls import url
from OnlinePractice.views import *

urlpatterns = [
    url(r'^$', onlinepractice, name='onlinepractice'),
]