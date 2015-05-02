# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'publication date')),
                ('cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('buyer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ad_char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=100)),
                ('measurement_unit', models.CharField(max_length=32, null=True, blank=True)),
                ('ad', models.ForeignKey(to='ads.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Char',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='chars',
            field=models.ManyToManyField(to='ads.Char', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='ads.Category', null=True),
        ),
        migrations.AddField(
            model_name='ad_char',
            name='char',
            field=models.ForeignKey(to='ads.Char'),
        ),
        migrations.AddField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(to='ads.Category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='chars',
            field=models.ManyToManyField(to='ads.Char', through='ads.Ad_char'),
        ),
    ]
