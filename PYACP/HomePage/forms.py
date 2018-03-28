#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField

# 验证器username


class SearchForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '搜索文章', 'style': 'float:none', 'class': 'form-control','required oninvalid':"setCustomValidity('请输入搜索内容')", 'oninput':"setCustomValidity('')"}),
                             max_length=50, error_messages={'required': ''})


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

    def clean(self):

        # 验证码
        try:
            captcha_x = self.cleaned_data['captcha']
        except Exception as e:
            print 'except: ' + str(e)
            raise forms.ValidationError(u"验证码有误，请重新输入")
        return self.cleaned_data

