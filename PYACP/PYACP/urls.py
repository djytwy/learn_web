# -*- coding: utf-8 -*-
"""PYACP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import HomePage
from HomePage import views
from django.views.static import serve
# from django.contrib import admin
from django.conf import settings

import xadmin # xadmin模块
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    url(r'^captcha/', include('captcha.urls')),
    url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^onlinepractice/', include('OnlinePractice.urls')),
    url(r'^home/', include('HomePage.urls')),
    url(r'^course/', include('Course.urls')),
    url(r'upload/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^email', HomePage.views.reg_success, name='email_reg'),
    url(r'^$', HomePage.views.homepage, name='home'),
]

# handler404 = HomePage.views.page_not_found

