from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    address = models.CharField('地址', max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = '作者'


class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'), (1, '女')))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author)

    class Meta:
        verbose_name = '作者详情'


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()




