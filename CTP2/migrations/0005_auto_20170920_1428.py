# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-20 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTP2', '0004_auto_20170919_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_brokerfund',
            name='nan',
        ),
        migrations.RemoveField(
            model_name='t_investorfund',
            name='nan',
        ),
        migrations.RemoveField(
            model_name='t_investorfunddtl',
            name='nan',
        ),
    ]
