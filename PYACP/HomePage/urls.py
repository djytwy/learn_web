#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias
from django.conf.urls import url
from HomePage.views import *

urlpatterns = [
    url(r'send_email', send_email, name='send_email'),
    url(r'^center', center, name='center'),
    url(r'^reg_success$', reg_success, name='reg_success'),
    url(r'^reg$', reg, name='reg'),
    url(r'^$', homepage, name='homepage'),
    url(r'^loginpage$', login_in, name='login_in'),
    url(r'^logoutpage$', login_out, name='login_out'),
    url(r'^experience', experience, name='experience'),
    url(r'^article', article, name='article'),
    url(r'^search', search, name='search'),
    url(r'^findpassword', findpassword, name='findpassword'),
    url(r'^success_find$', success_find, name='success_find'),
    url(r'^re_captcha$', re_captcha, name='re_captcha'),
]
