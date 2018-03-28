from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app1.models import Search

# Create your views here.


def index(request):
    return render(request, 'index.html')


def ajax(request):
    return render(request, 'ajax_test.html')


@csrf_exempt
def search(request):
    Search.objects.all()
    if request.POST.get('search') is not None:
        temp = request.POST.get('search')
        try:
            data = Search.objects.filter(search_data=temp).get()
            var = data.search_data
            print(var)
            return HttpResponse(var)
        except:
            var = '搜索不到您的内容'
            return HttpResponse(var)


@csrf_exempt
def search_h(request):
    var1 = []
    print('twy')
    if request.POST.get('search_h') is not None:
        temp2 = request.POST.get('search_h')
        data1 = Search.objects.filter(search_data__contains=temp2)
        for i in data1:
            var1.append(i.search_data)
        if var1 is not None:
            l = len(var1)
            for i in range(l):
                var1[i] = '<option>'+var1[i]+'</option>'
            return HttpResponse(var1)



