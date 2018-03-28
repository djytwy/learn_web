from django.db import models
from datetime import datetime

# Create your models here.


class Things(models.Model):
    things = models.CharField(max_length=300, verbose_name='事情')
    time = models.DateTimeField(auto_now=True, verbose_name='时间')
    time_sub = models.CharField(max_length=100, verbose_name='多久前')



