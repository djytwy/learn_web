#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias

from django.contrib import admin
from django.core import urlresolvers

import xadmin
from models import User, Article
from xadmin.plugins.auth import UserAdmin

# 改写用户表显示字段


class NewUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_scores', 'is_vip', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_vip', 'user_scores')
    list_editable = ('user_scores', 'is_vip', 'user_avatar')
    readonly_fields = ('date_joined',)

xadmin.site.unregister(User) # 反注册
xadmin.site.register(User, NewUserAdmin) # 注册


class NewArticle(object):
    list_display = ('title', 'article', 'time', 'user')
    list_editable = ('title', 'article',)

xadmin.site.register(Article, NewArticle)
# Register your models here.