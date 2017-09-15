# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class UserProfile(AbstractUser):
    detail_info = models.CharField(max_length=100, verbose_name=u"详细信息", default="")

    class Meta:
            verbose_name = "user"
            verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class RateSetting(models.Model):
    InvestorId = models.CharField(max_length=12,default="")
    ExchangeId = models.CharField(max_length=10,default="")
    InstrumentId = models.CharField(max_length=20,default="")
    SpHeMarks = models.CharField(max_length=1,default="")
    OCmarks = models.CharField(max_length=1, default="")
    InvestorRateByMoney = models.DecimalField(max_digits=8,decimal_places=5)
    InvestorRateByAmount = models.CharField(max_length=1,default="")
    ExchangeRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    ExchangeRateByAmount = models.CharField(max_length=1, default="")
    insert_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"费率"
        verbose_name_plural = verbose_name
