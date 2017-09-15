# -*- coding: utf-8 -*-


import xadmin
from .models import RateSetting
from xadmin import views


class PlatformSetting(object):
    site_title = "自动化测试平台"
    site_footer="结算测试组"
    menu_style = "accordion"

class RateSettingReg(object):
    pass

xadmin.site.register(RateSetting,RateSettingReg)
xadmin.site.register(views.CommAdminView,PlatformSetting)