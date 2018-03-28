from django.shortcuts import render, redirect
from App.models import Things
from App.form import ThingsForm
# Create your views here.


class Waring ():
    waring = False


def todolist(request):
    var = Waring
    Things.objects.all()
    things_list = Things.objects.all()
    if request.method == "POST":
        if request.POST.get('Delete') == 'Delete':
            delete_id = request.POST.get('id')
            Things.objects.filter(id=delete_id).delete()

        if request.POST.get('Edit') == 'Edit':
            text = request.POST.get('text')
            edit_id = request.POST.get('id')
            Things.objects.filter(id=edit_id).update(things=text)

        if request.POST.get('Add') == 'Add':
            thing = request.POST.get('dothis')
            if Things.objects.filter(things=thing).first() is None:
                Things.objects.create(things=thing)
                var.waring = False
            else:
                var.waring = True
    return render(request, 'index.html', locals())

