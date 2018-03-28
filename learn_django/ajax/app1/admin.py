from django.contrib import admin
from app1.models import *

# Register your models here.


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('search_data',)
