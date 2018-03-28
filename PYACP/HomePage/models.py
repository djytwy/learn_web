# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# 用户表


class User(AbstractUser):
    # 设置vip字段选项
    IS_VIP_CHOICES = (
        ('否', '普通用户'),
        ('是', 'Vip用户')
    )
    user_scores = models.IntegerField(default=False, verbose_name='用户积分')
    user_avatar = models.ImageField(verbose_name='用户头像', upload_to='avatar/%Y/%m', default='avatar/deafult.png', blank=True,
                                    null=True)
    is_vip = models.CharField(max_length=2, verbose_name='用户类型', choices=IS_VIP_CHOICES, default='否')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    send_email = models.EmailField(verbose_name='发送的邮箱')
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.send_email


class Article(models.Model):
    user = models.ForeignKey('HomePage.User', on_delete=models.CASCADE, verbose_name='用户名')
    title = models.CharField(verbose_name='文章的标题', max_length=100, default=None)
    article = models.TextField(verbose_name='文章的内容')
    time = models.DateTimeField(verbose_name='文章发布时间', default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

# Create your models here.


