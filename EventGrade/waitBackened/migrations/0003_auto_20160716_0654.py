# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitBackened', '0002_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='Category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Eventid',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Eventname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Nocomments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Nolikes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Nolinks',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='Venuename',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
