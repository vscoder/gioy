# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='buyer',
            field=models.ForeignKey(to='ads.Buyer'),
        ),
        migrations.AddField(
            model_name='ad',
            name='comment',
            field=models.TextField(max_length=1023, null=True, blank=True),
        ),
    ]
