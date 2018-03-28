from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#关闭CSRF验证，需要csrf_exempt装饰器
from django.views.decorators.csrf import csrf_exempt
from App.models import Things
#Django的表单验证的方法，可以选用
from App.form import ThingsForm
# Create your views here.


# class Waring ():
#     waring = False


# def todolist(request):
#     var = Waring
#     Things.objects.all()
#     things_list = Things.objects.all()
#     if request.method == "POST":
#         if request.POST.get('Delete') == 'Delete':
#             delete_id = request.POST.get('id')
#             Things.objects.filter(id=delete_id).delete()
#
#         if request.POST.get('Edit') == 'Edit':
#             text = request.POST.get('text')
#             edit_id = request.POST.get('id')
#             Things.objects.filter(id=edit_id).update(things=text)
#
#         if request.POST.get('Add') == 'Add':
#             thing = request.POST.get('dothis')
#             if Things.objects.filter(things=thing).first() is None:
#                 Things.objects.create(things=thing)
#                 var.waring = False
#             else:
#                 var.waring = True
#     return render(request, 'index.html', locals())

#AJAX的事件返回必须带一个HttpResponse或是其他的HTTP返回数据类型！！！！

def todolist(request):
    things_list = Things.objects.all()
    # from_source = request.session.get('from_brower', 'unkown')
    # return HttpResponse(from_source)
    return render(request, 'index.html', locals())


#添加事情，收到的json数据，返回的数据为一个HTML文档
def add_things(request):
    thing = request.POST.get('dothis')
    if Things.objects.filter(things=thing).first() is None:
        Things.objects.create(things=thing)
        num_temp = Things.objects.filter(things=thing).values() #Things.objects.filter(things=thing).values()返回类型是一个列表，内容的格式为字典[{},{}]
        num_temp = num_temp[0]
        num = num_temp['id']
        data = "<div class='row'><div class='col-md-10'><div class='form-group'><textarea class='form-control ' rows='3' name='text'>%s</textarea></div></div><div class='col-md-2'><div class='btn-group' role='group'><input type='submit' class='btn btn-warning' value='Delete' name='Delete'><input type='submit' class='btn btn-success' value='Edit' name='Edit'><span style='display: none'><textarea class='form-control ' rows='1' name='id'></textarea></span></div><div class='checkbox' id='%d'><label><input type='checkbox'>已经做了</label></div></div></div>" %(thing, num)
        print(num)
        return HttpResponse(data)
    else:
        return HttpResponse('这件事已经有了')


#编辑事情，收到新的事情，从数据库找到这个新的事情的ID，然后update新的事情
def Edit_thing(request):
    if request.method == 'POST':
        thing_update = request.POST.get('text')
        things_id = request.POST.get('things_id')
        Things.objects.filter(id=things_id).update(things=thing_update)
        return HttpResponse(thing_update)
    else:
        return render(request, 'index.html', locals())


#删除事情，收到事情的ID，然后在数据库中找到并执行delete（）方法
def Delete_thing(request):
    if request.method == 'POST':
        delete_id = request.POST.get('things_id')
        Things.objects.filter(id=delete_id).delete()
        return HttpResponse(delete_id)
    else:
        return render(request, 'index.html', locals())

