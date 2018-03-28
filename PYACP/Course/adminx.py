#!/usr/bin/env python
#-*- coding: utf-8 -*-
#author: Artorias

import xadmin
from models import User_choice, Course_choice, User_full, Course_full, User_project, Course_project


# 用户选择题管理
class User_choice_admin(object):
    list_display = ('choice_num', 'username', 'user_anwser', 'is_finish')
    list_editable = ('is_finish',)

xadmin.site.register(User_choice, User_choice_admin)


# 选择题库管理
class Course_choice_admin(object):
    list_display = ('choice_num', 'course_title', 'course_anwser')
    list_editable = ('course_anwser',)

xadmin.site.register(Course_choice, Course_choice_admin)


# 用户编程题管理
class User_full_admin(object):
    list_display = ('full_num', 'username', 'user_anwser', 'is_finish')
    list_editable = ('is_finish',)

xadmin.site.register(User_full, User_full_admin)


# 编程题库管理
class Course_full_admin(object):
    list_display = ('full_num', 'course_title', 'course_anwser')

xadmin.site.register(Course_full, Course_full_admin)


# 用户-项目题管理
class User_project_admin(object):
    list_display = ('project_num', 'username', 'user_anwser', 'is_finish')
    list_editable = ('is_finish',)

xadmin.site.register(User_project, User_project_admin)


# 项目题库管理
class Course_project_admin(object):
    list_display = ('project_num', 'course_title')

xadmin.site.register(Course_project, Course_project_admin)
