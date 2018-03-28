from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
#关闭CSRF验证，需要csrf_exempt装饰器
from django.views.decorators.csrf import csrf_exempt
from App.models import Things
#Django的表单验证的方法，可以选用
from App.form import ThingsForm
import datetime
import re
import json
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
    from_source = request.session.get('from_brower', 'unkown')
    time = datetime.datetime.now()
    if from_source == 'IE8':
        return render(request, 'brower.html')
    else:
        return render(request, 'index.html', locals())


#添加事情，收到的json数据，返回的数据为一个HTML文档
def add_things(request):
    thing = request.POST.get('dothis')
    time_now = datetime.datetime.now()
    time_now = str(time_now)
    if Things.objects.filter(things=thing).first() is None:
        Things.objects.create(things=thing, time=time_now)
        num_temp = Things.objects.filter(things=thing).values() #Things.objects.filter(things=thing).values()返回类型是一个列表，内容的格式为字典[{},{}]
        num_temp = num_temp[0]
        num = num_temp['id']
        data = "<div class='row'><div class='col-md-10'><div class='form-group'><textarea class='form-control ' rows='3' name='text'>%s --- 0分钟 - 1秒前</textarea></div></div><div class='col-md-2'><div class='btn-group' role='group'><input type='submit' class='btn btn-warning' value='Delete' name='Delete'><input type='submit' class='btn btn-success' value='Edit' name='Edit'><span style='display: none'><textarea class='form-control ' rows='1' name='id'></textarea></span></div><div class='checkbox' id='%d'><label><input type='checkbox'>已经做了</label></div></div></div>" % (thing, num, )
        print(num)
        return HttpResponse(data)
    else:
        return HttpResponse('这件事已经有了')


#编辑事情，收到新的事情，从数据库找到这个新的事情的ID，然后update新的事情
def Edit_thing(request):
    if request.method == 'POST':
        thing_update = request.POST.get('text')
        things_id = request.POST.get('things_id')
        p1 = re.compile('(.*?) ---', re.S)
        thing_update_1 = re.findall(p1, thing_update)
        Things.objects.filter(id=things_id).update(things=thing_update_1[0])
        thing_update = thing_update_1[0] + ' --- 0分钟 - 1秒前'
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


def update_time(request):
    now = datetime.datetime.now()
    data_send = []
    day_s = 0
    hour_s = 0
    minutes_s = 0
    sec_s = 0
    if request.method == 'POST':
        data_raw = request.POST.get('times')
        p1 = re.compile('(.*?) ---', re.S)
        p2 = re.compile('--- (.*)\.', re.S)
        if '秒' not in data_raw:
            data = json.loads(data_raw)
            print(data)
            print(type(data))
            for i in data:
                data_1 = re.findall(p1, i)
                data_2 = re.findall(p2, i)
                print(data_1, data_2)
                process_time = datetime.datetime.strptime(data_2[0], "%Y-%m-%d %H:%M:%S")
                sec = (now-process_time).seconds
                days = (now-process_time).days

                if days >= 1:
                    if sec >= 3600:
                        hour = sec//3600
                        minutes = (sec % 3600)//60
                        seconds = sec % 60
                        data = data_1[0] + ' --- ' + '%d天 - %d小时 - %d分钟 - %d秒前' % (days, hour, minutes, seconds)
                    elif sec >= 60 and sec < 3600:
                        minutes = (sec % 3600)//60
                        seconds = sec % 60
                        data = data_1[0] + ' --- ' + '%d天 - %d分钟 -%d秒前' % (days, minutes, seconds)
                    else:
                        seconds = sec
                        data = data_1[0] + ' --- ' + '%d天 - 0分钟 - %d秒前' % (days, seconds)
                else:
                    if sec >= 3600:
                        hour = sec//3600
                        minutes = (sec % 3600)//60
                        seconds = sec % 60
                        data = data_1[0] + ' --- ' + '%d小时 - %d分钟 - %d秒前' % (hour, minutes, seconds)
                    elif 60 <= sec < 3600:
                        minutes = (sec % 3600)//60
                        seconds = sec % 60
                        data = data_1[0] + ' --- ' + '%d分钟 - %d秒前' % (minutes, seconds)
                    else:
                        seconds = sec
                        data = data_1[0] + ' --- ' + '0分钟 - %d秒前' % seconds
                data_send.append(data)
            data_send = json.dumps(data_send)
            print(data_send)
            return HttpResponse(data_send)
        else:
            data = json.loads(data_raw)
            p3 = re.compile('(.*?)钟', re.S)
            p4 = re.compile('钟 - (.*?)秒', re.S)
            print(data)
            data_send.clear()
            for i in data:
                if i != '':
                    data_raw1 = re.findall(p3, i)
                    data_sec = re.findall(p4, i)
                    # p_day = re.compile('(.*?)天', re.S)
                    # day = re.findall(p_day, data_2[0])
                    # if len(day) == 0:
                    #     day_s = ''
                    # else:
                    #     day = int(day[0])
                    # p_hour = re.compile('天 (.*?)小时', re.S)
                    # hour = re.findall(p_hour, data_2[0])
                    # if len(hour) == 0:
                    #     hour_s = ''
                    # else:
                    #     hour = int(hour[0])
                    # p_minutes = re.compile('小时(.*?)分钟', re.S)
                    # minutes = re.findall(p_minutes, data_2[0])
                    # if len(minutes) == 0:
                    #     minutes_s = ''
                    # else:
                    #     minutes = int(minutes[0])
                    # p_sec = re.compile('分钟(.*?)秒', re.S)
                    # sec = re.findall(p_sec, data_2[0])
                    # sec = int(sec[0])
                    # if sec >= 60:
                    #     if minutes == '':
                    #         minutes_s = '1'
                    #     else:
                    #         minutes += 1
                    #         if minutes >= 60:
                    #             if hour == '':
                    #                 hour_s = '1'
                    #             else:
                    #                 hour += 1
                    #                 hour_s = str(hour)
                    #                 if hour > 24:
                    #                     if day == '':
                    #                         day_s = '1'
                    #                     else:
                    #                         day += 1
                    #                         day_s = day
                    #                         day_s = str(day_s)
                    #                     hour_s = hour % 24
                    #                     hour_s = str(hour_s)
                    #             minutes_s = minutes % 60
                    #             minutes_s = str(minutes_s)
                    #     sec_s = sec % 60
                    # sec_s = sec_s + 5
                    # sec_s = str(sec_s)
                    # if day_s == '':
                    #     if hour_s == '':
                    #         if minutes_s == '':
                    #             data_fin = data_1[0] + ' --- ' + '0分钟%s秒前' % sec_s
                    #         else:
                    #             data_fin = data_1[0] + ' --- ' + '%s分钟%s秒前' % (minutes_s, sec_s)
                    #     else:
                    #         data_fin = data_1[0] + ' --- ' + '%s小时%s分钟%s秒前' % (hour_s, minutes_s, sec_s)
                    # else:
                    #     data_fin = data_1[0] + ' --- ' + '%s天 %s小时%s分钟%s秒前' % (day_s, hour_s, minutes_s, sec_s)
                    print(data_sec, i)
                    data_sec = int(data_sec[0])+20
                    data_fin = data_raw1[0] + '钟 - ' + str(data_sec) + '秒' + '前'
                    data_send.append(data_fin)
            data_send = json.dumps(data_send)
            return HttpResponse(data_send)


# if day >= 365:
        #     year = day//365
        #     mouth = (day % 365)//30
        #     days = (day % 365) % 30