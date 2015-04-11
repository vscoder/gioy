from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Char(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=100)
    chars = models.ManyToManyField(Char)

class Ad(models.Model):
    buyer = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publication date')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    chars = models.ManyToManyField(Char, through='Ad_char')

class Ad_char(models.Model):
    ad = models.ForeignKey(Ad)
    char = models.ForeignKey(Char)
    value = models.CharField(max_length=100)


