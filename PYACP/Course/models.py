# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from HomePage.models import User
from django.db import models


# 用户-选择题表
class User_choice(models.Model):
    # 选择题选项
    USER_ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    username = models.ForeignKey('HomePage.User', on_delete=models.CASCADE, verbose_name='用户名')
    choice_num = models.CharField(max_length=5, verbose_name='选择题编号')
    user_answer = models.CharField(max_length=5, verbose_name='用户选择题回答', null=True, default=None, choices=USER_ANSWER_CHOICES)

    def __str__(self):
        return str(self.choice_num)

    class Meta:
        verbose_name_plural = '用户-选择题'
        verbose_name = '用户-选择题'


# 选择题库
class Course_choice(models.Model):
    # 选择题答案选项
    COURSE_ANSWER_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
    choice_num = models.CharField(max_length=5, verbose_name='选择题编号', unique=True)
    course_title = models.CharField(max_length=50, verbose_name='选择题题目', unique=True)
    choice_A = models.CharField(max_length=50, verbose_name='答案A', blank=True)
    choice_B = models.CharField(max_length=50, verbose_name='答案B', blank=True)
    choice_C = models.CharField(max_length=50, verbose_name='答案C', blank=True)
    choice_D = models.CharField(max_length=50, verbose_name='答案D', blank=True)
    course_answer = models.CharField(max_length=2, verbose_name='选择题答案', choices=COURSE_ANSWER_CHOICES, null=False)
    is_finish = models.BooleanField(verbose_name='完成练习', default=False)

    def __str__(self):
        return str(self.course_answer)

    class Meta:
        verbose_name = '选择题库'
        verbose_name_plural = '选择题库'


# 用户-编程题表
class User_full(models.Model):
    username = models.ForeignKey('HomePage.User', on_delete=models.CASCADE, verbose_name='用户名')
    full_num = models.ForeignKey('Course_full', on_delete=models.CASCADE, verbose_name='编程题编号', to_field='full_num')
    user_answer = models.CharField(max_length=1000, verbose_name='用户编程题回答', null=True, default=None)

    def __str__(self):
        return str(self.full_num)

    class Meta:
        verbose_name_plural = '用户-编程题'
        verbose_name = '用户-编程题'


# 编程题库
class Course_full(models.Model):
    full_num = models.IntegerField(verbose_name='编程题编号', unique=True)
    course_title = models.CharField(max_length=50, verbose_name='选择题题目', unique=True)
    course_answer = models.CharField(max_length=1000, verbose_name='编程题答案',  null=False)
    is_finish = models.BooleanField(verbose_name='完成练习', default=False)

    def __str__(self):
        return str(self.full_num)

    class Meta:
        verbose_name = '编程题库'
        verbose_name_plural = '编程题库'


# 用户-项目表
class User_project(models.Model):
    username = models.ForeignKey('HomePage.User', on_delete=models.CASCADE, verbose_name='用户名')
    project_num = models.ForeignKey('Course_project', on_delete=models.CASCADE, verbose_name='项目题编号', to_field='project_num')
    user_answer = models.CharField(max_length=10000, verbose_name='用户项目题回答', null=True, default=None)

    def __str__(self):
        return str(self.project_num)


    class Meta:
        verbose_name = '用户-项目'
        verbose_name_plural = '用户-项目'


# 项目题库
class Course_project(models.Model):
    project_num = models.IntegerField(verbose_name='项目题编号', unique=True)
    course_title = models.CharField(max_length=50, verbose_name='项目题题目', unique=True)
    course_answer = models.CharField(max_length=1000, verbose_name='项目题答案', null=False)
    is_finish = models.BooleanField(verbose_name='完成练习', default=False)

    def __str__(self):
        return str(self.project_num)

    class Meta:
        verbose_name = '项目题库'
        verbose_name_plural = '项目题库'


# Create your models here.
