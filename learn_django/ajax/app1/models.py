from django.db import models

# Create your models here.


class Search(models.Model):
    search_data = models.CharField(max_length=100, verbose_name="搜索内容")
