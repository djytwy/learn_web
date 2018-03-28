from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def test(request):
    return render(request, 'table.html')


def test2(request, id, key):
    print(id)
    print(key)
    return render(request, 'table.html')


def test_Httpresponse(request):
    response = HttpResponse('这是一个response的测试')
    return response
'''
用render跳转到table.html，注意render的用法！
'''


def hello(request):
    print(request.POST.get('items'))
    print(request.get_full_path())
    user_list = User.objects.all()
    print(user_list.query)
    return render(request, 'table.html', {'user_list': user_list})


'''
用HttpResponse跳转到table.html，注意HttpResponse的用法！
'''


def view2(request):
    print(request.POST.get('items'))
    print(request.get_full_path())
    user_list = User.objects.all()
    t = loader.get_template('table.html')
    c = {'user_list': user_list}
    return HttpResponse(t.render(c, request),
                        content_type='text/html')

'''
用render_to_response跳转到table.html，注意render_to_response的用法！
'''


def hello2(request):
    print(request.POST.get('items'))
    print(request.get_full_path())
    user_list = User.objects.all()
    # return render_to_response('table.html', {'user_list': user_list})
    return render_to_response('table.html', locals())  #locals()可以将所有的参数传到html页面中

'''
redirect的用法：跳转，下例将跳转到百度首页
'''


def hello3(request):
    print(request.POST.get('items'))
    print(request.get_full_path())
    user_list = User.objects.all()
    return redirect('/hello')

