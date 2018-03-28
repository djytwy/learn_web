from django.conf.urls import url
from App import views

urlpatterns = [
    url(r'^todolist/', views.todolist),
    url(r'^add_things/', views.add_things),
    url(r'^Edit/', views.Edit_thing),
    url(r'^delete', views.Delete_thing),
]

