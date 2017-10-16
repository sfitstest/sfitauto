# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-16 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarginRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExchangeId', models.CharField(default='', max_length=100)),
                ('InstrumentId', models.CharField(default='', max_length=20)),
                ('SpHeMarks', models.CharField(default='', max_length=1)),
                ('LSmarks', models.CharField(default='', max_length=1)),
                ('InvestorMarginRateByMoney', models.DecimalField(decimal_places=5, max_digits=8)),
                ('InvestorMarginRateByAmount', models.CharField(default='', max_length=1)),
                ('ExchangeMarginRateByMoney', models.DecimalField(decimal_places=5, max_digits=8)),
                ('ExchangeMarginRateByAmount', models.CharField(default='', max_length=1)),
                ('InvestorOpMarginRateByMoney', models.DecimalField(decimal_places=5, max_digits=8)),
                ('InvestorOpMarginRateByAmount', models.CharField(default='', max_length=1)),
            ],
            options={
                'verbose_name': '\u7ed3\u679c\u5bfc\u5165',
                'verbose_name_plural': '\u7ed3\u679c\u5bfc\u5165',
            },
        ),
        migrations.CreateModel(
            name='t_brokerfund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EXCHANGEID', models.CharField(default='', max_length=100)),
                ('EXCHMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHSMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHHMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHDELIVMARGIN', models.CharField(default='', max_length=100)),
                ('OPTPREMIUMINCOME', models.CharField(default='', max_length=100)),
                ('OPTPREMIUMPAY', models.CharField(default='', max_length=100)),
                ('FUNDOUT', models.CharField(default='', max_length=100)),
                ('FUNDIN', models.CharField(default='', max_length=100)),
                ('CLOSEPROFIT', models.CharField(default='', max_length=100)),
                ('POSITIONPROFIT', models.CharField(default='', max_length=100)),
                ('OPTSTRIKEPROFIT', models.CharField(default='', max_length=100)),
                ('EXCHTRANSFEE', models.CharField(default='', max_length=100)),
                ('DELIVFEE', models.CharField(default='', max_length=100)),
                ('STRIKEFEE', models.CharField(default='', max_length=100)),
                ('LASTDEPOSIT', models.CharField(default='', max_length=100)),
                ('REMAIN', models.CharField(default='', max_length=100)),
                ('DEPOSIT', models.CharField(default='', max_length=100)),
                ('PREPA', models.CharField(default='', max_length=100)),
                ('WITHDRAWQUOTA', models.CharField(default='', max_length=100)),
                ('MORTGAGE', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u4ea4\u6613\u6240\u8d44\u91d1',
                'verbose_name_plural': '\u4ea4\u6613\u6240\u8d44\u91d1',
            },
        ),
        migrations.CreateModel(
            name='T_INVESTORCLOSEDTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorid', models.CharField(default='', max_length=100)),
                ('volume', models.CharField(default='', max_length=100)),
                ('openprice', models.CharField(default='', max_length=100)),
                ('closeprice', models.CharField(default='', max_length=100)),
                ('lastsettlementprice', models.CharField(default='', max_length=100)),
                ('closeprofitbydate', models.CharField(default='', max_length=100)),
                ('closeprofitbytrade', models.CharField(default='', max_length=100)),
                ('volumemultiple', models.CharField(default='', max_length=100)),
                ('INVESTUNITID', models.CharField(default='', max_length=100)),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('instrumentid', models.CharField(default='', max_length=100)),
                ('tradeid', models.CharField(default='', max_length=100)),
                ('orgtradeid', models.CharField(default='', max_length=100)),
                ('offsetflag', models.CharField(default='', max_length=100)),
                ('posidirection', models.CharField(default='', max_length=100)),
                ('hedgeflag', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u671f\u8d27\u5e73\u4ed3\u660e\u7ec6',
                'verbose_name_plural': '\u671f\u8d27\u5e73\u4ed3\u660e\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='t_investorfund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('CALLMARGIN', models.CharField(default='', max_length=100)),
                ('RESERVE', models.CharField(default='', max_length=100)),
                ('LOWESTINTEREST', models.CharField(default='', max_length=100)),
                ('MORTGAGE', models.CharField(default='', max_length=100)),
                ('FUNDMORTGAGEIN', models.CharField(default='', max_length=100)),
                ('FUNDMORTGAGEOUT', models.CharField(default='', max_length=100)),
                ('FUNDMORTGAGEMARGIN', models.CharField(default='', max_length=100)),
                ('FUNDIN', models.CharField(default='', max_length=100)),
                ('LASTDEPOSIT', models.CharField(default='', max_length=100)),
                ('FUNDOUT', models.CharField(default='', max_length=100)),
                ('LASTDEPOSITBYTRADE', models.CharField(default='', max_length=100)),
                ('REMAIN', models.CharField(default='', max_length=100)),
                ('DEPOSIT', models.CharField(default='', max_length=100)),
                ('DEPOSITBYTRADE', models.CharField(default='', max_length=100)),
                ('MARKETDEPOSIT', models.CharField(default='', max_length=100)),
                ('PREPA', models.CharField(default='', max_length=100)),
                ('WITHDRAWQUOTA', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u6295\u8d44\u8005\u8d44\u91d1\u4f59\u989d',
                'verbose_name_plural': '\u6295\u8d44\u8005\u8d44\u91d1\u4f59\u989d',
            },
        ),
        migrations.CreateModel(
            name='t_InvestorFundDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('SPECACTUAL', models.CharField(default='', max_length=100)),
                ('MARGIN', models.CharField(default='', max_length=100)),
                ('SPECMARGIN', models.CharField(default='', max_length=100)),
                ('DELIVMARGIN', models.CharField(default='', max_length=100)),
                ('BOPTMARKETVALUE', models.CharField(default='', max_length=100)),
                ('SOPTMARKETVALUE', models.CharField(default='', max_length=100)),
                ('OPTSTRIKEPROFIT', models.CharField(default='', max_length=100)),
                ('SMARGIN', models.CharField(default='', max_length=100)),
                ('HMARGIN', models.CharField(default='', max_length=100)),
                ('OPTPREMIUMINCOME', models.CharField(default='', max_length=100)),
                ('ACTUAL', models.CharField(default='', max_length=100)),
                ('SPECFEE', models.CharField(default='', max_length=100)),
                ('EXCHMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHSMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHHMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHDELIVMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHTRANSFEE', models.CharField(default='', max_length=100)),
                ('EXCHDELIVFEE', models.CharField(default='', max_length=100)),
                ('OPTPREMIUMPAY', models.CharField(default='', max_length=100)),
                ('CLOSEPROFIT', models.CharField(default='', max_length=100)),
                ('CLOSEPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('POSITIONPROFIT', models.CharField(default='', max_length=100)),
                ('POSITIONPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('TRANSFEE', models.CharField(default='', max_length=100)),
                ('DELIVFEE', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u6295\u8d44\u8005\u5206\u4ea4\u6613\u6240\u8d44\u91d1',
                'verbose_name_plural': '\u6295\u8d44\u8005\u5206\u4ea4\u6613\u6240\u8d44\u91d1',
            },
        ),
        migrations.CreateModel(
            name='T_INVESTORTRADEFEEDTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorid', models.CharField(default='', max_length=100)),
                ('volume', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('transfee', models.CharField(default='', max_length=100)),
                ('exchtransfee', models.CharField(default='', max_length=100)),
                ('INVESTUNITID', models.CharField(default='', max_length=100)),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('tradeid', models.CharField(default='', max_length=100)),
                ('instrumentid', models.CharField(default='', max_length=100)),
                ('volumemultiple', models.CharField(default='', max_length=100)),
                ('offsetflag', models.CharField(default='', max_length=100)),
                ('POSIDIRECTION', models.CharField(default='', max_length=100)),
                ('hedgeflag', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u6210\u4ea4\u624b\u7eed\u8d39\u660e\u7ec6',
                'verbose_name_plural': '\u6210\u4ea4\u624b\u7eed\u8d39\u660e\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='t_invstinstrsettleinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorid', models.CharField(default='', max_length=100)),
                ('BPOSITIONPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('SPOSITIONPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('BCLOSEPROFITBYDATE', models.CharField(default='', max_length=100)),
                ('SCLOSEPROFITBYDATE', models.CharField(default='', max_length=100)),
                ('BCLOSEPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('SCLOSEPROFITBYTRADE', models.CharField(default='', max_length=100)),
                ('BMARGIN', models.CharField(default='', max_length=100)),
                ('SMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHBMARGIN', models.CharField(default='', max_length=100)),
                ('EXCHSMARGIN', models.CharField(default='', max_length=100)),
                ('INVESTUNITID', models.CharField(default='', max_length=100)),
                ('VOLUMEMULTIPLE', models.CharField(default='', max_length=100)),
                ('TRANSFEE', models.CharField(default='', max_length=100)),
                ('SETTLEMENTFEE', models.CharField(default='', max_length=100)),
                ('DELIVFEE', models.CharField(default='', max_length=100)),
                ('STRIKEFEE', models.CharField(default='', max_length=100)),
                ('PERFORMFEE', models.CharField(default='', max_length=100)),
                ('EXCHTRANSFEE', models.CharField(default='', max_length=100)),
                ('EXCHDELIVFEE', models.CharField(default='', max_length=100)),
                ('EXCHSTRIKEFEE', models.CharField(default='', max_length=100)),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('EXCHPERFORMFEE', models.CharField(default='', max_length=100)),
                ('EXCHSETTLEMENTFEE', models.CharField(default='', max_length=100)),
                ('BAVGCOST', models.CharField(default='', max_length=100)),
                ('SAVGCOST', models.CharField(default='', max_length=100)),
                ('instrumentid', models.CharField(default='', max_length=100)),
                ('hedgeflag', models.CharField(default='', max_length=100)),
                ('BTOTALAMT', models.CharField(default='', max_length=100)),
                ('STOTALAMT', models.CharField(default='', max_length=100)),
                ('BPOSITIONPROFITBYDATE', models.CharField(default='', max_length=100)),
                ('SPOSITIONPROFITBYDATE', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u671f\u8d27\u6301\u4ed3\u6c47\u603b',
                'verbose_name_plural': '\u671f\u8d27\u6301\u4ed3\u6c47\u603b',
            },
        ),
        migrations.CreateModel(
            name='T_INVSTPOSITIONDTL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorid', models.CharField(default='', max_length=100)),
                ('settlementprice', models.CharField(default='', max_length=100)),
                ('positionprofitbydate', models.CharField(default='', max_length=100)),
                ('positionprofitbytrade', models.CharField(default='', max_length=100)),
                ('margin', models.CharField(default='', max_length=100)),
                ('exchmargin', models.CharField(default='', max_length=100)),
                ('MARGINRATEBYMONEY', models.CharField(default='', max_length=100)),
                ('volumemultiple', models.CharField(default='', max_length=100)),
                ('INVESTUNITID', models.CharField(default='', max_length=100)),
                ('instrumentid', models.CharField(default='', max_length=100)),
                ('hedgeflag', models.CharField(default='', max_length=100)),
                ('posidirection', models.CharField(default='', max_length=100)),
                ('tradeid', models.CharField(default='', max_length=100)),
                ('volume', models.CharField(default='', max_length=100)),
                ('openprice', models.CharField(default='', max_length=100)),
                ('lastsettlementprice', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u671f\u8d27\u6301\u4ed3\u660e\u7ec6',
                'verbose_name_plural': '\u671f\u8d27\u6301\u4ed3\u660e\u7ec6',
            },
        ),
        migrations.CreateModel(
            name='t_trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investorid', models.CharField(default='', max_length=100)),
                ('price', models.CharField(default='', max_length=100)),
                ('volume', models.CharField(default='', max_length=100)),
                ('INVESTUNITID', models.CharField(default='', max_length=100)),
                ('ACCOUNTID', models.CharField(default='', max_length=100)),
                ('tradeid', models.CharField(default='', max_length=100)),
                ('instrumentid', models.CharField(default='', max_length=100)),
                ('volumemultiple', models.CharField(default='', max_length=100)),
                ('direction', models.CharField(default='', max_length=100)),
                ('offsetflag', models.CharField(default='', max_length=100)),
                ('hedgeflag', models.CharField(default='', max_length=100)),
            ],
            options={
                'verbose_name': '\u671f\u8d27\u6210\u4ea4\u660e\u7ec6',
                'verbose_name_plural': '\u671f\u8d27\u6210\u4ea4\u660e\u7ec6',
            },
        ),
    ]
