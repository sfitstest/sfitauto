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


class MarginRate(models.Model):
    ExchangeId = models.CharField(max_length=10, default="")
    InstrumentId = models.CharField(max_length=20, default="")
    SpHeMarks = models.CharField(max_length=1, default="")
    LSmarks=models.CharField(max_length=1,default="")
    InvestorMarginRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    InvestorMarginRateByAmount = models.CharField(max_length=1, default="")
    ExchangeMarginRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    ExchangeMarginRateByAmount = models.CharField(max_length=1, default="")
    InvestorOpMarginRateAjByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    InvestorOpMarginRateAjByAmount = models.CharField(max_length=1, default="")

    class Meta:
        verbose_name = u"保证金率"
        verbose_name_plural = verbose_name


class FuRateSetting(models.Model):
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
        verbose_name = u"期货手续费费率"
        verbose_name_plural = verbose_name


class OpRateSetting(models.Model):
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
        verbose_name = u"期权手续费费率"
        verbose_name_plural = verbose_name