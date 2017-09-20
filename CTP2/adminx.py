# _*_ coding: utf-8 _*_

import xadmin
import pandas as pd
import xlrd
from xadmin import views
from .models import MarginRate
from .models import t_InvestorFundDtl
from .models import t_investorfund
from .models import t_trade
from .models import T_INVESTORTRADEFEEDTL
from .models import t_brokerfund
from .models import T_INVESTORCLOSEDTL
from .models import T_INVSTPOSITIONDTL
from .models import t_invstinstrsettleinfo




class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True


class MarginRateSettingReg(object):
    #列表种展示的
    list_display=["ExchangeId","InstrumentId","SpHeMarks","LSmarks","InvestorMarginRateByMoney","InvestorMarginRateByAmount","ExchangeMarginRateByMoney","ExchangeMarginRateByAmount","InvestorOpMarginRateByMoney","InvestorOpMarginRateByAmount"]
    search_fields = ['ExchangeId','InstrumentId','SpHeMarks', 'LSmarks']
    list_filter = ['ExchangeId','InstrumentId','SpHeMarks', 'LSmarks']
    #根据点击排序
    ordering = ['-ExchangeId']
    #指定只读（不可修改）的字段
    readonly_fields = ()
    #可直接在列表页编辑的字段
    list_editable = ['ExchangeId','SpHeMarks', 'LSmarks']
    import_excel = True
    search_fields = ()

    def post(self, request, *args):
        if 'excel' in request.FILES:
            file = request.FILES['excel']
            data = pd.read_excel(file,sheetname='t_InvestorFundDtl|投资者分交易所资金'.decode("utf-8"))

            column = data.keys()

            i = 0
            index = 0
            alldf = {}

            alldf[i] = pd.DataFrame()


            for isnull in data[column[0]].isnull():
                if isnull:
                    i += 1
                    alldf[i] = pd.DataFrame()
                else:
                    alldf[i] = alldf[i].append(data.iloc[index], ignore_index=True)
                index += 1

            alldfnum = i
            table = 1
            for table in range(0, alldfnum + 1):
                for keys in alldf[table]:
                    isallnull = True
                    for values in alldf[table][keys]:
                        if not pd.isnull(values):
                            isallnull = False
                            break
                    if isallnull:
                        del alldf[table][keys]
            sql_list = []

            lenth = len(alldf[0])

            for i in range(0, lenth):
                rv = alldf[0].iloc[i]
                ss=""
                for keys in alldf[0]:
                #     ss+= keys + '=' + rv[keys] + ','
                #
                # sql = 't_InvestorFundDtl('+ss+')'
                 sql=t_InvestorFundDtl(
                    ACCOUNTID=rv["ACCOUNTID"],
                    ACTUAL=rv["ACTUAL"],
                    BOPTMARKETVALUE=rv["BOPTMARKETVALUE"],
                    CLOSEPROFIT=rv["CLOSEPROFIT"],
                    CLOSEPROFITBYTRADE=rv["CLOSEPROFITBYTRADE"],
                    DELIVFEE=rv["DELIVFEE"],
                    DELIVMARGIN=rv["DELIVMARGIN"],
                    EXCHDELIVFEE=rv["EXCHDELIVFEE"],
                    EXCHDELIVMARGIN=rv["EXCHDELIVMARGIN"],
                    EXCHHMARGIN=rv["EXCHHMARGIN"],
                    EXCHMARGIN=rv["EXCHMARGIN"],
                    EXCHSMARGIN=rv["EXCHSMARGIN"],
                    EXCHTRANSFEE=rv["EXCHTRANSFEE"],
                    HMARGIN=rv["HMARGIN"],
                    MARGIN=rv["MARGIN"],
                    OPTPREMIUMINCOME=rv["OPTPREMIUMINCOME"],
                    OPTPREMIUMPAY=rv["OPTPREMIUMPAY"],
                    OPTSTRIKEPROFIT=rv["OPTSTRIKEPROFIT"],
                    POSITIONPROFIT=rv["POSITIONPROFIT"],
                    POSITIONPROFITBYTRADE=rv["POSITIONPROFITBYTRADE"],
                    SMARGIN=rv["SMARGIN"],
                    SOPTMARKETVALUE=rv["SOPTMARKETVALUE"],
                    SPECACTUAL=rv["SPECACTUAL"],
                    SPECFEE=rv["SPECFEE"],
                    SPECMARGIN=rv["SPECMARGIN"],
                    TRANSFEE=rv["TRANSFEE"],
                )


                sql_list.append(sql)
            t_InvestorFundDtl.objects.bulk_create(sql_list)


        return super(MarginRateSettingReg, self).post(request, args)


class t_InvestorFundDtlreg(object):
    list_display=[ "ACCOUNTID","SPECACTUAL","MARGIN","SPECMARGIN","DELIVMARGIN","BOPTMARKETVALUE","SOPTMARKETVALUE","OPTSTRIKEPROFIT","SMARGIN","HMARGIN","OPTPREMIUMINCOME","DELIVMARGIN","ACTUAL","SPECFEE","EXCHMARGIN","EXCHSMARGIN","EXCHHMARGIN","EXCHDELIVMARGIN","EXCHTRANSFEE","EXCHDELIVFEE","OPTPREMIUMPAY","CLOSEPROFIT","CLOSEPROFITBYTRADE","POSITIONPROFIT","POSITIONPROFITBYTRADE","TRANSFEE","DELIVFEE"]

class t_investorfundreg(object):
    list_display=[ "ACCOUNTID","CALLMARGIN","RESERVE","LOWESTINTEREST","MORTGAGE","FUNDMORTGAGEIN","FUNDMORTGAGEOUT","FUNDMORTGAGEMARGIN","FUNDIN","LASTDEPOSIT","FUNDOUT","LASTDEPOSITBYTRADE","REMAIN","DEPOSIT","DEPOSITBYTRADE","MARKETDEPOSIT","PREPA","WITHDRAWQUOTA"]

class t_brokerfundreg(object):
    list_display=[ "EXCHANGEID","EXCHMARGIN","EXCHSMARGIN","EXCHHMARGIN","EXCHDELIVMARGIN","OPTPREMIUMINCOME","OPTPREMIUMPAY","FUNDOUT","FUNDIN","CLOSEPROFIT","POSITIONPROFIT","OPTSTRIKEPROFIT","EXCHTRANSFEE","DELIVFEE","STRIKEFEE","LASTDEPOSIT","REMAIN","DEPOSIT","PREPA","WITHDRAWQUOTA","MORTGAGE"]

class t_tradereg(object):
    list_display=[ "investorid","price","volume","INVESTUNITID","ACCOUNTID","tradeid","instrumentid","volumemultiple","direction","offsetflag","hedgeflag"]

class T_INVESTORTRADEFEEDTLreg(object):
    list_display=[ "investorid","volume","price","transfee","exchtransfee","INVESTUNITID","ACCOUNTID","tradeid","instrumentid","volumemultiple","offsetflag","POSIDIRECTION","hedgeflag"]

class T_INVESTORCLOSEDTLreg(object):
    list_display=[ "investorid","volume","openprice","closeprice","lastsettlementprice","closeprofitbydate","closeprofitbytrade","volumemultiple","INVESTUNITID","ACCOUNTID","instrumentid","tradeid","orgtradeid","offsetflag","posidirection","hedgeflag"]

class T_INVSTPOSITIONDTLreg(object):
    list_display=[ "investorid","settlementprice","positionprofitbydate","positionprofitbytrade","margin","exchmargin","MARGINRATEBYMONEY","volumemultiple","INVESTUNITID","instrumentid","hedgeflag","posidirection","tradeid","volume","openprice","lastsettlementprice"]

class t_invstinstrsettleinforeg(object):
    list_display=[ "investorid","BPOSITIONPROFITBYTRADE","SPOSITIONPROFITBYTRADE","BCLOSEPROFITBYDATE","SCLOSEPROFITBYDATE","BCLOSEPROFITBYTRADE","SCLOSEPROFITBYTRADE","BMARGIN","SMARGIN","EXCHBMARGIN","EXCHSMARGIN","INVESTUNITID","VOLUMEMULTIPLE","TRANSFEE","TRANSFEE","SETTLEMENTFEE","DELIVFEE","STRIKEFEE","PERFORMFEE","EXCHTRANSFEE","EXCHDELIVFEE","EXCHSTRIKEFEE","ACCOUNTID","EXCHPERFORMFEE","EXCHSETTLEMENTFEE","BAVGCOST","SAVGCOST","instrumentid","hedgeflag","BTOTALAMT","STOTALAMT","BPOSITIONPROFITBYDATE","SPOSITIONPROFITBYDATE"]




xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(MarginRate,MarginRateSettingReg)
xadmin.site.register(t_InvestorFundDtl,t_InvestorFundDtlreg)
xadmin.site.register(t_investorfund,t_investorfundreg)
xadmin.site.register(t_brokerfund,t_brokerfundreg)
xadmin.site.register(t_trade,t_tradereg)
xadmin.site.register(T_INVESTORTRADEFEEDTL,T_INVESTORTRADEFEEDTLreg)
xadmin.site.register(T_INVESTORCLOSEDTL,T_INVESTORCLOSEDTLreg)
xadmin.site.register(T_INVSTPOSITIONDTL,T_INVSTPOSITIONDTLreg)
xadmin.site.register(t_invstinstrsettleinfo,t_invstinstrsettleinforeg)











