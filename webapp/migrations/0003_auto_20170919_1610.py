# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-19 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170913_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opratesetting',
            options={'verbose_name': '\u671f\u6743\u624b\u7eed\u8d39\u8d39\u7387', 'verbose_name_plural': '\u671f\u6743\u624b\u7eed\u8d39\u8d39\u7387'},
        ),
        migrations.RenameField(
            model_name='marginrate',
            old_name='InvestorOpMarginRateByAmount',
            new_name='InvestorOpMarginRateAjByAmount',
        ),
        migrations.RenameField(
            model_name='marginrate',
            old_name='InvestorOpMarginRateByMoney',
            new_name='InvestorOpMarginRateAjByMoney',
        ),
    ]
