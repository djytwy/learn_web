# -*- coding:utf-8 -*-
from django import forms
from models import Course_choice


class Form_Choice(forms.ModelForm):

    def clean(self):
        cleaned_data = super(Form_Choice, self).clean()
        data = cleaned_data.get('answer')
        print cleaned_data

    class Meta:
        model = Course_choice
        fields = ['choice_num']
        widgets = {
            'choice_num':forms.TextInput(attrs={'id':'none','name':'none','style':'display:none,color:red'}),
        }

