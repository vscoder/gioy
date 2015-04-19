# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Char(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=100)
    chars = models.ManyToManyField(Char, blank=True, null=True)

    def __unicode__(self):
        return self.name

class Ad(models.Model):
    buyer = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('publication date', default=timezone.now)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    chars = models.ManyToManyField(Char, through='Ad_char')

    def was_published_recently(self, days=1):
        """
        return true if Ad was published in the past
        else return false
        """
        now = timezone.now()
        return now - datetime.timedelta(days=days) <= self.pub_date <= now


    def __unicode__(self):
        return self.name

class Ad_char(models.Model):
    ad = models.ForeignKey(Ad)
    char = models.ForeignKey(Char)
    value = models.CharField(max_length=100)
    measurement_unit = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.char.name
