from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'$', views.todolist, name='todolist'),
]

