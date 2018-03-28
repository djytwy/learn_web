from django.contrib import admin
from App.models import *
# Register your models here.


@admin.register(Things)
class ThingsAdmin(admin.ModelAdmin):
    list_display = ('things', )

