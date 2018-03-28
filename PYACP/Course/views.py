# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import User_choice, Course_choice
from django.views.decorators.csrf import csrf_exempt
from forms import Form_Choice
from HomePage.forms import SearchForm
from HomePage import sendemail
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json
import re

# Create your views here.


# 显示五道选择题
# @login_required
def course_choice(request):
    username = request.user.username
    request.session['reg'] = 0
    request.session['send_email'] = 0
    request.session['findpassword'] = 0
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    error = {}
    if request.method == 'POST':
        username = request.user
        answers = request.POST.get('answers')
        answer_list = json.loads(answers)
        for i in answer_list:
            try:
                Course_choice.objects.filter(choice_num=i).update(is_finish=True)
                User_choice.objects.get(choice_num=i)
                User_choice.objects.filter(choice_num=i).update(user_answer=answer_list[i])
            except Exception as e:
                print e
                User_choice.objects.create(
                    user_answer=answer_list[i], choice_num=i, username=username
                )
            correct_answer = Course_choice.objects.get(choice_num=i).course_answer
            if answer_list[i] != correct_answer:
                error[i] = 'error'
        return HttpResponse(json.dumps(error), content_type='application/json')
    else:
        course_choice_list = Course_choice.objects.all()
    return render(request, 'course/choice.html', locals())

# 分页器代码
# def getPage(request, article_list):
#     paginator = Paginator(article_list, 5)
#     try:
#         page = int(request.GET.get('page', 1))
#         article_list = paginator.page(page)
#     except (EmptyPage, InvalidPage, PageNotAnInteger):
#         article_list = paginator.page(1)
#     return article_list
#


