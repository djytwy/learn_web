# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from models import User, Article, EmailVerifyRecord
from Course.models import Course_choice, Course_full, Course_project, User_choice, User_full, User_project
from forms import SearchForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import sendemail
import json
import re
# Create your views here.


# 用户注册
def reg(request):
    # ajax提交数据，进行字段格式验证，验证通过再注册
    if request.method == 'POST':
        # 获取表单提交信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_again = request.POST.get('passwordagain')
        email = request.POST.get('email')
        hashkey = request.POST.get('hash_reg')
        captcha_reg = request.POST.get('captcha_reg')
        captcha = CaptchaStore.objects.get(hashkey=hashkey)
        captchas = [captcha.challenge, captcha.response]

        if captcha_reg not in captchas:
            error = {'error_captcha': '验证码错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')

        email_pattern = re.compile(r'^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$')
        name_pattern = re.compile(r'^[a-zA-Z0-9_-]{6,15}$')
        password_pattern = re.compile(r'^[a-zA-Z0-9_-]{6,}$')
        re_name = re.match(name_pattern, username)
        re_password = re.match(password_pattern, password)
        re_email = re.match(email_pattern, email)

        if re_name is None:
            error = {'error_name': '用户名格式错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')

        elif re_password is None:
            error = {'error_password': '密码格式错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')

        elif re_email is None:
            error = {'error_email': '邮箱格式错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')
        # 判断两次输入的密码是否一致
        if password != password_again:
            error = {'error_password_again': '两次输入的密码不一致'}
            return HttpResponse(json.dumps(error), content_type='application/json')
        else:
            try:
                User.objects.get(username=username)
                error = {'error_name': '该用户已存在！'}
                return HttpResponse(json.dumps(error), content_type='application/json')
            except Exception as e:
                print e
            try:
                User.objects.get(email=email)
                error = {'error_email': '该邮箱已经注册！'}
                return HttpResponse(json.dumps(error), content_type='application/json')
            except Exception as e:
                print e
                sendemail.send_register_email(email)
                User.objects.create_user(username=username, password=password, email=email, is_active=0)
                error = {'turn': 'yes'}
                return HttpResponse(json.dumps(error), content_type='application/json')
    return redirect('/')


# 注册成功发送邮件激活
def send_email(request):
    if request.session['reg'] == 1:
        request.session['reg'] = 0
        request.session['send_email'] = 1
        # print request.session['send_email']
        return render(request, 'send_email.html', locals())
    else:
        return redirect('/')


# 注册成功页
def reg_success(request):
    if request.method == 'GET':
        if request.session['send_email'] == 1:
            request.session['send_email'] = 0
            email_code = request.GET.get('email', None)
            email_r = EmailVerifyRecord.objects.get(code=email_code)
            User.objects.filter(email=email_r).update(is_active=1)
            return render(request, 'reg_success.html', locals())
        else:
            searchform = SearchForm()
            hashkey = CaptchaStore.generate_key()
            imgage_url = captcha_image_url(hashkey)
            return redirect('/')


# 用户登录
def login_in(request):
    # post方法提交，获取username, password，登录不需要验证字段，只需要验证密码
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # 登录失败时返回json字符串进行局部刷新
        try:
            if user is not None:
                user = User.objects.get(username=username)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                ifturn = {'turn': 'yes'}
                return HttpResponse(json.dumps(ifturn), content_type='application/json')
            else:
                error = {'error': '用户名/密码错误'}
                return HttpResponse(json.dumps(error), content_type='application/json')
        except:
            error = {'error': '用户名/密码错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')
    return redirect('/')


# 退出登录
@login_required
def login_out(request):
    logout(request)
    if '/center' or '/course/' in request.META['HTTP_REFERER']:
        return redirect('/')
    else:
        return redirect(request.META['HTTP_REFERER'])


# 找回密码
def findpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        newpassword = request.POST.get('newpassword')
        hashkey = request.POST.get('hash_findpassword')
        human = request.POST.get('captcha_findpassword')
        send_password = newpassword
        newpassword = make_password(newpassword)
        captcha = CaptchaStore.objects.get(hashkey=hashkey)
        captchas = [captcha.challenge, captcha.response]

        pattern = re.compile('^[a-zA-Z0-9_-]{6,}$')
        re_password = re.findall(pattern, send_password)
        # print human
        # print captchas, hashkey
        if human not in captchas:
            error = {'error_captcha': '验证码错误'}
            return HttpResponse(json.dumps(error), content_type='application/json')
        elif re_password is None:
            error = {'error_password': '密码格式错误！'}
            return HttpResponse(json.dumps(error), content_type='application/json')
        try:
            User.objects.filter(username=username, email=email).update(password=newpassword)
            sendemail.send_findpassword_email(email, username, send_password)
            request.session['findpassword'] = 1
            success = {'success': 'success'}
            return HttpResponse(json.dumps(success), content_type='application/json')
            # return redirect('/home/success_find')
        except Exception as e:
            print e
            error = {'error_user': '用户名或者邮箱不存在！'}
            return HttpResponse(json.dumps(error), content_type='application/json')


def success_find(request):
    if request.session['findpassword'] == 0:
        return redirect('/')
    else:
        request.session['findpassword'] = 0
        return render(request, 'findpassword.html')


# 主页
def homepage(request):
    username = request.user.username
    request.session['reg'] = 0
    request.session['send_email'] = 0
    request.session['findpassword'] = 0
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    try:
        user_avatar = User.objects.get(username=username).user_avatar
        return render(request, 'homepage/homepage.html', locals())
    except Exception as e:
        print e
        return render(request, 'homepage/homepage.html', locals())


# 个人中心页的内容
@login_required
def center(request):
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)

    username = request.user.username
    user = User.objects.get(username=username)

    choice_sum = float(Course_choice.objects.count())
    full_sum = float(Course_full.objects.count())
    project_sum = float(Course_project.objects.count())

    choice_finish = float(Course_choice.objects.filter(is_finish=True).count())
    full_finish = float(Course_full.objects.filter(is_finish=True).count())
    project_finish = float(Course_project.objects.filter(is_finish=True).count())

    if choice_sum != 0 and full_sum != 0 and project_sum != 0:
        progress_choice = (choice_finish/choice_sum)*100
        progress_full = (full_finish/full_sum)*100
        progress_project = (project_finish/project_sum)*100

    elif choice_sum == 0 and full_sum != 0 and project_sum != 0:
        progress_choice = '抱歉，选择题的内容待完善！'
        progress_full = (full_finish / full_sum) * 100
        progress_project = (project_finish / project_sum) * 100

    elif choice_sum == 0 and full_sum == 0 and project_sum != 0:
        progress_choice = '抱歉，选择题的内容待完善！'
        progress_full = '抱歉，填空题的内容待完善！'
        progress_project = (project_finish / project_sum) * 100

    elif choice_sum == 0 and full_sum != 0 and project_sum == 0:
        progress_choice = '抱歉，选择题的内容待完善！'
        progress_full = (full_finish / full_sum) * 100
        progress_project = '抱歉，项目题的内容待完善！'

    elif choice_sum != 0 and full_sum == 0 and project_sum == 0:
        progress_choice = (choice_finish / choice_sum) * 100
        print progress_choice
        progress_full = '抱歉，填空题的内容待完善！'
        progress_project = '抱歉，项目题的内容待完善！'

    elif choice_sum != 0 and full_sum != 0 and project_sum == 0:
        progress_choice = (choice_finish / choice_sum) * 100
        progress_full = (full_finish / full_sum) * 100
        progress_project = '抱歉，项目题的内容待完善！'

    elif choice_sum != 0 and full_sum == 0 and project_sum != 0:
        progress_choice = (choice_finish / choice_sum) * 100
        progress_full = '抱歉，填空题的内容待完善！'
        progress_project = (project_finish / project_sum) * 100

    else:
        progress_choice = '抱歉，选择题的内容待完善！'
        progress_full = '抱歉，填空题的内容待完善！'
        progress_project = '抱歉，项目题的内容待完善！'

    return render(request, 'center.html', locals())


# 经验之谈页的内容
def experience(request):
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    try:
        article_list = Article.objects.all()
        article_list = getpage(request, article_list)
    except Exception as e:
        print e
    return render(request, 'homepage/experience.html', locals())


# 文章页的内容
def article(request):
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    try:
        title = request.GET.get('article', None)
        articles = Article.objects.get(title=title)
    except Exception as e:
        print e
    return render(request, 'homepage/article.html', locals())


# 搜索功能的实现
def search(request):
    searchform = SearchForm()
    hashkey = CaptchaStore.generate_key()
    imgage_url = captcha_image_url(hashkey)
    try:
        search_data = request.GET.get('search', None)
        if request.method == 'GET':
            searchform = SearchForm(request.GET)
            # print searchform.is_valid()
            if searchform.is_valid():
                search_data = searchform.cleaned_data['search']
                result_list = Article.objects.filter(title__icontains=search_data)
                article_list = getpage(request, result_list)
                return render(request, 'search.html', locals())
            else:
                return render(request, 'homepage/homepage.html', locals())
    except Exception as e:
        print e
    return render(request, 'search.html', locals())


# 重新获取验证码
def re_captcha(request):
    if request.method == 'GET':
        hashkey = CaptchaStore.generate_key()
        imgage_url = captcha_image_url(hashkey)
        captcha = {
                    'hashkey': hashkey,
                    'imgage_url': imgage_url,
                  }
        return HttpResponse(json.dumps(captcha), content_type='application/json')


# 404页面
def page_not_found(request):
    return render_to_response('404.html')


# 分页器
def getpage(request, article_list):
    paginator = Paginator(article_list, 5)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

# [<User: 305111632>]

