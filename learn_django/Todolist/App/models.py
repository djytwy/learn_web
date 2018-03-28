from django.db import models

# Create your models here.


class Things(models.Model):
    things = models.CharField(max_length=300)



