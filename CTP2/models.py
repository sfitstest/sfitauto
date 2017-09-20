# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class MarginRate(models.Model):
    ExchangeId = models.CharField(max_length=100, default="")
    InstrumentId = models.CharField(max_length=20, default="")
    SpHeMarks = models.CharField(max_length=1, default="")
    LSmarks=models.CharField(max_length=1,default="")
    InvestorMarginRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    InvestorMarginRateByAmount = models.CharField(max_length=1, default="")
    ExchangeMarginRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    ExchangeMarginRateByAmount = models.CharField(max_length=1, default="")
    InvestorOpMarginRateByMoney = models.DecimalField(max_digits=8, decimal_places=5)
    InvestorOpMarginRateByAmount = models.CharField(max_length=1, default="")

    class Meta:
        verbose_name = u"结果导入"
        verbose_name_plural = verbose_name


class t_InvestorFundDtl(models.Model):
    ACCOUNTID=models.CharField(max_length=100, default='')
    SPECACTUAL=models.CharField(max_length=100, default='')
    MARGIN=models.CharField(max_length=100, default='')
    SPECMARGIN=models.CharField(max_length=100, default='')
    DELIVMARGIN=models.CharField(max_length=100, default='')
    BOPTMARKETVALUE=models.CharField(max_length=100, default='')
    SOPTMARKETVALUE=models.CharField(max_length=100, default='')
    OPTSTRIKEPROFIT=models.CharField(max_length=100, default='')
    SMARGIN=models.CharField(max_length=100, default='')
    HMARGIN=models.CharField(max_length=100, default='')
    OPTPREMIUMINCOME=models.CharField(max_length=100, default='')
    ACTUAL=models.CharField(max_length=100, default='')
    SPECFEE=models.CharField(max_length=100, default='')
    EXCHMARGIN=models.CharField(max_length=100, default='')
    EXCHSMARGIN=models.CharField(max_length=100, default='')
    EXCHHMARGIN=models.CharField(max_length=100, default='')
    EXCHDELIVMARGIN=models.CharField(max_length=100, default='')
    EXCHTRANSFEE=models.CharField(max_length=100, default='')
    EXCHDELIVFEE=models.CharField(max_length=100, default='')
    OPTPREMIUMPAY=models.CharField(max_length=100, default='')
    CLOSEPROFIT=models.CharField(max_length=100, default='')
    CLOSEPROFITBYTRADE=models.CharField(max_length=100, default='')
    POSITIONPROFIT=models.CharField(max_length=100, default='')
    POSITIONPROFITBYTRADE=models.CharField(max_length=100, default='')
    TRANSFEE=models.CharField(max_length=100, default='')
    DELIVFEE=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"投资者分交易所资金"
        verbose_name_plural = verbose_name


class t_investorfund(models.Model):
    ACCOUNTID=models.CharField(max_length=100, default='')
    CALLMARGIN=models.CharField(max_length=100, default='')
    RESERVE=models.CharField(max_length=100, default='')
    LOWESTINTEREST=models.CharField(max_length=100, default='')
    MORTGAGE=models.CharField(max_length=100, default='')
    FUNDMORTGAGEIN=models.CharField(max_length=100, default='')
    FUNDMORTGAGEOUT=models.CharField(max_length=100, default='')
    FUNDMORTGAGEMARGIN=models.CharField(max_length=100, default='')
    FUNDIN=models.CharField(max_length=100, default='')
    LASTDEPOSIT=models.CharField(max_length=100, default='')
    FUNDOUT=models.CharField(max_length=100, default='')
    LASTDEPOSITBYTRADE=models.CharField(max_length=100, default='')
    REMAIN=models.CharField(max_length=100, default='')
    DEPOSIT=models.CharField(max_length=100, default='')
    DEPOSITBYTRADE=models.CharField(max_length=100, default='')
    MARKETDEPOSIT=models.CharField(max_length=100, default='')
    PREPA=models.CharField(max_length=100, default='')
    WITHDRAWQUOTA=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"投资者资金余额"
        verbose_name_plural = verbose_name

class t_brokerfund(models.Model):
    EXCHANGEID=models.CharField(max_length=100, default='')
    EXCHMARGIN=models.CharField(max_length=100, default='')
    EXCHSMARGIN=models.CharField(max_length=100, default='')
    EXCHHMARGIN=models.CharField(max_length=100, default='')
    EXCHDELIVMARGIN=models.CharField(max_length=100, default='')
    OPTPREMIUMINCOME=models.CharField(max_length=100, default='')
    OPTPREMIUMPAY=models.CharField(max_length=100, default='')
    FUNDOUT=models.CharField(max_length=100, default='')
    FUNDIN=models.CharField(max_length=100, default='')
    CLOSEPROFIT=models.CharField(max_length=100, default='')
    POSITIONPROFIT=models.CharField(max_length=100, default='')
    OPTSTRIKEPROFIT=models.CharField(max_length=100, default='')
    EXCHTRANSFEE=models.CharField(max_length=100, default='')
    DELIVFEE=models.CharField(max_length=100, default='')
    STRIKEFEE=models.CharField(max_length=100, default='')
    LASTDEPOSIT=models.CharField(max_length=100, default='')
    REMAIN=models.CharField(max_length=100, default='')
    DEPOSIT=models.CharField(max_length=100, default='')
    PREPA=models.CharField(max_length=100, default='')
    WITHDRAWQUOTA=models.CharField(max_length=100, default='')
    MORTGAGE=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"交易所资金"
        verbose_name_plural = verbose_name

class t_trade(models.Model):
    investorid=models.CharField(max_length=100, default='')
    price=models.CharField(max_length=100, default='')
    volume=models.CharField(max_length=100, default='')
    INVESTUNITID=models.CharField(max_length=100, default='')
    ACCOUNTID=models.CharField(max_length=100, default='')
    tradeid=models.CharField(max_length=100, default='')
    instrumentid=models.CharField(max_length=100, default='')
    volumemultiple=models.CharField(max_length=100, default='')
    direction=models.CharField(max_length=100, default='')
    offsetflag=models.CharField(max_length=100, default='')
    hedgeflag=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"期货成交明细"
        verbose_name_plural = verbose_name

class T_INVESTORTRADEFEEDTL(models.Model):
    investorid=models.CharField(max_length=100, default='')
    volume=models.CharField(max_length=100, default='')
    price=models.CharField(max_length=100, default='')
    transfee=models.CharField(max_length=100, default='')
    exchtransfee=models.CharField(max_length=100, default='')
    INVESTUNITID=models.CharField(max_length=100, default='')
    ACCOUNTID=models.CharField(max_length=100, default='')
    tradeid=models.CharField(max_length=100, default='')
    instrumentid=models.CharField(max_length=100, default='')
    volumemultiple=models.CharField(max_length=100, default='')
    offsetflag=models.CharField(max_length=100, default='')
    POSIDIRECTION=models.CharField(max_length=100, default='')
    hedgeflag=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"成交手续费明细"
        verbose_name_plural = verbose_name

class T_INVESTORCLOSEDTL(models.Model):
    investorid=models.CharField(max_length=100, default='')
    volume=models.CharField(max_length=100, default='')
    openprice=models.CharField(max_length=100, default='')
    closeprice=models.CharField(max_length=100, default='')
    lastsettlementprice=models.CharField(max_length=100, default='')
    closeprofitbydate=models.CharField(max_length=100, default='')
    closeprofitbytrade=models.CharField(max_length=100, default='')
    volumemultiple=models.CharField(max_length=100, default='')
    INVESTUNITID=models.CharField(max_length=100, default='')
    ACCOUNTID=models.CharField(max_length=100, default='')
    instrumentid=models.CharField(max_length=100, default='')
    tradeid=models.CharField(max_length=100, default='')
    orgtradeid=models.CharField(max_length=100, default='')
    offsetflag=models.CharField(max_length=100, default='')
    posidirection=models.CharField(max_length=100, default='')
    hedgeflag=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"期货平仓明细"
        verbose_name_plural = verbose_name

class T_INVSTPOSITIONDTL(models.Model):
    investorid=models.CharField(max_length=100, default='')
    settlementprice=models.CharField(max_length=100, default='')
    positionprofitbydate=models.CharField(max_length=100, default='')
    positionprofitbytrade=models.CharField(max_length=100, default='')
    margin=models.CharField(max_length=100, default='')
    exchmargin=models.CharField(max_length=100, default='')
    MARGINRATEBYMONEY=models.CharField(max_length=100, default='')
    volumemultiple=models.CharField(max_length=100, default='')
    INVESTUNITID=models.CharField(max_length=100, default='')
    instrumentid=models.CharField(max_length=100, default='')
    hedgeflag=models.CharField(max_length=100, default='')
    posidirection=models.CharField(max_length=100, default='')
    tradeid=models.CharField(max_length=100, default='')
    volume=models.CharField(max_length=100, default='')
    openprice=models.CharField(max_length=100, default='')
    lastsettlementprice=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"期货持仓明细"
        verbose_name_plural = verbose_name

class t_invstinstrsettleinfo(models.Model):
    investorid=models.CharField(max_length=100, default='')
    BPOSITIONPROFITBYTRADE=models.CharField(max_length=100, default='')
    SPOSITIONPROFITBYTRADE=models.CharField(max_length=100, default='')
    BCLOSEPROFITBYDATE=models.CharField(max_length=100, default='')
    SCLOSEPROFITBYDATE=models.CharField(max_length=100, default='')
    BCLOSEPROFITBYTRADE=models.CharField(max_length=100, default='')
    SCLOSEPROFITBYTRADE=models.CharField(max_length=100, default='')
    BMARGIN=models.CharField(max_length=100, default='')
    SMARGIN=models.CharField(max_length=100, default='')
    EXCHBMARGIN=models.CharField(max_length=100, default='')
    EXCHSMARGIN=models.CharField(max_length=100, default='')
    INVESTUNITID=models.CharField(max_length=100, default='')
    VOLUMEMULTIPLE=models.CharField(max_length=100, default='')
    TRANSFEE=models.CharField(max_length=100, default='')
    TRANSFEE=models.CharField(max_length=100, default='')
    SETTLEMENTFEE=models.CharField(max_length=100, default='')
    DELIVFEE=models.CharField(max_length=100, default='')
    STRIKEFEE=models.CharField(max_length=100, default='')
    PERFORMFEE=models.CharField(max_length=100, default='')
    EXCHTRANSFEE=models.CharField(max_length=100, default='')
    EXCHDELIVFEE=models.CharField(max_length=100, default='')
    EXCHSTRIKEFEE=models.CharField(max_length=100, default='')
    ACCOUNTID=models.CharField(max_length=100, default='')
    EXCHPERFORMFEE=models.CharField(max_length=100, default='')
    EXCHSETTLEMENTFEE=models.CharField(max_length=100, default='')
    BAVGCOST=models.CharField(max_length=100, default='')
    SAVGCOST=models.CharField(max_length=100, default='')
    instrumentid=models.CharField(max_length=100, default='')
    hedgeflag=models.CharField(max_length=100, default='')
    BTOTALAMT=models.CharField(max_length=100, default='')
    STOTALAMT=models.CharField(max_length=100, default='')
    BPOSITIONPROFITBYDATE=models.CharField(max_length=100, default='')
    SPOSITIONPROFITBYDATE=models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = u"期货持仓汇总"
        verbose_name_plural = verbose_name



