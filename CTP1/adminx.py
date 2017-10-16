# -*- coding: utf-8 -*-
import xadmin
import xlrd
from .models import MarginRate
from .models import FuRateSetting
from .models import OpRateSetting
#from .models import UserProfile
from xadmin import views


class PlatformSetting(object):
    site_title = "自动化测试平台"
    site_footer = "结算测试组"
    # show_bookmarks = False
    menu_style = "accordion"


class MarginRateSettingReg(object):
    # 列表种展示的
    list_display = ["ExchangeId", "InstrumentId", "SpHeMarks", "LSmarks", "InvestorMarginRateByMoney",
                    "InvestorMarginRateByAmount", "ExchangeMarginRateByMoney", "ExchangeMarginRateByAmount",
                    "InvestorOpMarginRateAjByMoney", "InvestorOpMarginRateAjByAmount"]
    search_fields = ['ExchangeId', 'InstrumentId', 'SpHeMarks', 'LSmarks']
    list_filter = ['ExchangeId', 'InstrumentId', 'SpHeMarks', 'LSmarks']
    # 根据点击排序
    ordering = ['-ExchangeId']
    # 指定只读（不可修改）的字段
    readonly_fields = ()
    # 可直接在列表页编辑的字段
    list_editable = ['ExchangeId', 'SpHeMarks', 'LSmarks']
    import_excel = True
    #search_fields = ()
    export_ora = True

    def post(self, request, *args):
        if 'excel' in request.FILES:
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            curr_sheet = wb.sheet_by_name('data')
            data = [curr_sheet.row_values(row) for row in range(0, curr_sheet.nrows)]
            for x in range(curr_sheet.nrows):
                if curr_sheet.cell(x, 0).value == '保证金率设置':
                    index_mar = x
                elif curr_sheet.cell(x, 0).value == '期货手续费率设置':
                    index_fu = x
                elif curr_sheet.cell(x, 0).value == '期权手续费率':
                    index_opt = x
                elif curr_sheet.cell(x, 0).value == '系统参数设置':
                    index_sysparm = x
            print index_fu, index_mar, index_opt
            data_margin = data[index_mar + 2:index_fu]
            data_future_fee = data[index_fu + 2:index_opt]
            data_option_fee = data[index_opt + 2:index_sysparm]
            sql_list = []
            for col in data_margin:
                # col = table.row_values(i)
                sql = MarginRate(
                    ExchangeId=col[0],
                    InstrumentId=col[1],
                    SpHeMarks=int(col[2]),
                    LSmarks=int(col[3]),
                    InvestorMarginRateByMoney=col[4],
                    InvestorMarginRateByAmount=int(col[5]),
                    ExchangeMarginRateByMoney=col[6],
                    ExchangeMarginRateByAmount=int(col[7]),
                    InvestorOpMarginRateAjByMoney=col[8],
                    InvestorOpMarginRateAjByAmount=int(col[9]),
                )
                sql_list.append(sql)
            MarginRate.objects.bulk_create(sql_list)

        return super(MarginRateSettingReg, self).post(request, args)


class FuRateSettingReg(object):
    # 列表种展示的
    list_display = ["InvestorId", "ExchangeId", "InstrumentId", "SpHeMarks", "OCmarks", "InvestorRateByMoney",
                    "InvestorRateByAmount", "ExchangeRateByMoney", "ExchangeRateByAmount"]
    search_fields = ['InvestorId', 'ExchangeId', 'InstrumentId', 'SpHeMarks', 'OCmarks']
    list_filter = ['InvestorId', 'ExchangeId', 'InstrumentId', 'SpHeMarks', 'OCmarks']
    # 根据点击排序
    ordering = ['-InvestorId']
    # 指定只读（不可修改）的字段
    readonly_fields = ()
    # 可直接在列表页编辑的字段
    list_editable = ['InvestorId', 'ExchangeId', 'SpHeMarks', 'OCmarks']

    # import_excel位True，excel导入,会覆盖插件中(plugins/excel.py)import_excel的默认值
    import_excel = True
    search_fields = ()

    def post(self, request, *args):
        if 'excel' in request.FILES:
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            curr_sheet = wb.sheet_by_name('data')
            data = [curr_sheet.row_values(row) for row in range(0, curr_sheet.nrows)]
            for x in range(curr_sheet.nrows):
                if curr_sheet.cell(x, 0).value == '保证金率设置':
                    index_mar = x
                elif curr_sheet.cell(x, 0).value == '期货手续费率设置':
                    index_fu = x
                elif curr_sheet.cell(x, 0).value == '期权手续费率':
                    index_opt = x
                elif curr_sheet.cell(x, 0).value == '系统参数设置':
                    index_sysparm = x
            data_margin = data[index_mar + 2:index_fu]
            data_future_fee = data[index_fu + 2:index_opt]
            data_option_fee = data[index_opt + 2:index_sysparm]
            sql_list = []
            for col in data_future_fee:
                sql = FuRateSetting(
                    InvestorId=col[0],
                    ExchangeId=col[1],
                    InstrumentId=col[2],
                    SpHeMarks=int(col[3]),
                    OCmarks=int(col[4]),
                    InvestorRateByMoney=col[5],
                    InvestorRateByAmount=int(col[6]),
                    ExchangeRateByMoney=col[7],
                    ExchangeRateByAmount=int(col[8]),
                )
                sql_list.append(sql)
            FuRateSetting.objects.bulk_create(sql_list)
        return super(FuRateSettingReg, self).post(request, args)


class OpRateSettingReg(object):
    # 列表种展示的
    list_display = ["InvestorId", "ExchangeId", "InstrumentId", "SpHeMarks", "OCmarks", "InvestorRateByMoney",
                    "InvestorRateByAmount", "ExchangeRateByMoney", "ExchangeRateByAmount"]
    search_fields = ['InvestorId', 'ExchangeId', 'InstrumentId', 'SpHeMarks', 'OCmarks']
    list_filter = ['InvestorId', 'ExchangeId', 'InstrumentId', 'SpHeMarks', 'OCmarks']
    # 根据点击排序
    ordering = ['-InvestorId']
    # 指定只读（不可修改）的字段
    readonly_fields = ()
    # 可直接在列表页编辑的字段
    list_editable = ['InvestorId', 'ExchangeId', 'SpHeMarks', 'OCmarks']

    # import_excel位True，excel导入,会覆盖插件中(plugins/excel.py)import_excel的默认值
    import_excel = True
    #list_export = ()
    search_fields = ()

    # list_filter = ()


    # menu_style = None

    def post(self, request, *args):
        if 'excel' in request.FILES:
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['excel'].read())
            curr_sheet = wb.sheet_by_name('data')
            data = [curr_sheet.row_values(row) for row in range(0, curr_sheet.nrows)]
            for x in range(curr_sheet.nrows):
                if curr_sheet.cell(x, 0).value == '保证金率设置':
                    index_mar = x
                elif curr_sheet.cell(x, 0).value == '期货手续费率设置':
                    index_fu = x
                elif curr_sheet.cell(x, 0).value == '期权手续费率':
                    index_opt = x
                elif curr_sheet.cell(x, 0).value == '系统参数设置':
                    index_sysparm = x
            data_margin = data[index_mar + 2:index_fu]
            data_future_fee = data[index_fu + 2:index_opt]
            data_option_fee = data[index_opt + 2:index_sysparm]
            sql_list = []
            for col in data_option_fee:
                sql = FuRateSetting(
                    InvestorId=col[0],
                    ExchangeId=col[1],
                    InstrumentId=col[2],
                    SpHeMarks=int(col[3]),
                    OCmarks=int(col[4]),
                    InvestorRateByMoney=col[5],
                    InvestorRateByAmount=int(col[6]),
                    ExchangeRateByMoney=col[7],
                    ExchangeRateByAmount=int(col[8]),
                )
                sql_list.append(sql)
            OpRateSetting.objects.bulk_create(sql_list)

        return super(OpRateSettingReg, self).post(request, args)


xadmin.site.register(MarginRate, MarginRateSettingReg)
xadmin.site.register(FuRateSetting, FuRateSettingReg)
xadmin.site.register(OpRateSetting, OpRateSettingReg)
xadmin.site.register(views.CommAdminView, PlatformSetting)
