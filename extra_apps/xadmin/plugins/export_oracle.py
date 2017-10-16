# -*- coding: utf-8 -*-

import io
import os
import datetime
import sys
import cx_Oracle
from future.utils import iteritems

from django.http import HttpResponse
from django.template import loader
from django.utils import six
from django.utils.encoding import force_text, smart_text
from django.utils.html import escape
from django.utils.translation import ugettext as _
from django.utils.xmlutils import SimplerXMLGenerator
from django.db.models import BooleanField, NullBooleanField

from xadmin.plugins.utils import get_context_dict
from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView
from xadmin.util import json
from xadmin.views.list import ALL_VAR


class ExportToOraMenuPlugin(BaseAdminPlugin):
    # export_ora = True

    # def init_request(self, *args, **kwargs):
    #     return bool(self.export_ora)
    # 返回True才会加载插件

    list_export = ('asp636', 'asp2636')
    export_names = {'asp636': 'asp636', 'asp2636': 'asp2636'}

    def init_request(self, *args, **kwargs):
        self.list_export = [
            f for f in self.list_export]

    def block_top_toolbar(self, context, nodes):
        if self.list_export:
            context.update({
                'show_export_all': self.admin_view.paginator.count > self.admin_view.list_per_page and not ALL_VAR in self.admin_view.request.GET,
                'form_params': self.admin_view.get_form_params({'_do_': 'export'}, ('export_type',)),
                'export_types': [{'type': et, 'name': self.export_names[et]} for et in self.list_export],
            })
        nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.export2o.html',
                                             context=get_context_dict(context)))


class Export2oraPlugin(BaseAdminPlugin):
    export_mimes = {'asp636': 'asp636',
                    'asp2636': 'asp2636 '}
    model_table = {'CTP1.marginrate': ['t_CurrInstrMarginRate', 't_CurrExchMarginRate', 't_InstrumentMarginRateUL'],
                   'CTP1.furatesetting': ['t_CurrInstrCommRate', 't_CurrExchCommRate'],
                   'CTP1.opratesetting': ['t_CurrOpInstrCommRate', 't_CurrOpExchCommRate']}

    def init_request(self, *args, **kwargs):
        return self.request.GET.get('_do_') == 'export'

    def _format_value(self, o):
        print o.field, o.attr, o.text
        if (o.field is None and getattr(o.attr, 'boolean', False)) or \
                (o.field and isinstance(o.field, (BooleanField, NullBooleanField))):
            value = o.value
        elif str(o.text).startswith("<span class='text-muted'>"):
            value = escape(str(o.text)[25:-7])
        else:
            value = escape(str(o.text))
        return value

    def _get_objects(self, context):
        headers = [c for c in context['result_headers'].cells if c.export]
        rows = context['results']

        return [dict([
            (force_text(headers[i].text), self._format_value(o)) for i, o in
            enumerate(filter(lambda c: getattr(c, 'export', False), r.cells))]) for r in rows]

    def _get_datas(self, context):
        rows = context['results']
        # nes_rows = [[filter(lambda c: getattr(c, 'export', False), r.cells)] for r in rows]

        new_rows = [[self._format_value(o) for o in
                     filter(lambda c: getattr(c, 'export', False), r.cells)] for r in rows]
        print new_rows
        new_rows.insert(0, [force_text(c.text) for c in context['result_headers'].cells if c.export])
        return new_rows

    def con_to_oracle(self, conn_host_port, t_name, va):
        host_port = '172.19.124.13/%s' % conn_host_port
        conn = cx_Oracle.connect('settlement', 'settlement1111', host_port)
        # print host_port
        cursor = conn.cursor()
        sql = 'insert into %s values %s' % (t_name, va)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

    def get_data_export(self, context, oracle_host_port):

        ke = context['opts']
        ke = str(ke)

        # print self.model_table[str(context['opts'])]
        #datas = self._get_datas(context)
        #datas = datas[1:]
        print context['opts']
        tradingday = '20150505'
        brokerid = '2500'
        investorRange = '1'
        ratioattr = '0'
        if str(context['opts']) == 'CTP1.marginrate':
            t_currinsmar_name = 't_Currinstrmarginrate'
            t_currexchmar_name = 't_currexchmarginrate'
            t_insrmarUL_name = 't_InstrumentMarginRateUL'
            list_t_CurrInstrMarginRate = [0, 0, 0, 0, 0, 0, 0, 0]
            list_t_CurrExchMarginRate = [0, 0, 0, 0, 0, 0, 0, 0]
            list_t_InstrumentMarginRateUL = [0, 0, 0, 0, 0, 0, 0, 0]
            for it in datas:

                if (it[2] == '1') and (it[3] == '0'):
                    list_t_CurrInstrMarginRate[0] = it[4]
                    list_t_CurrInstrMarginRate[1] = it[5]
                    list_t_CurrExchMarginRate[0] = it[6]
                    list_t_CurrExchMarginRate[1] = it[7]
                    list_t_InstrumentMarginRateUL[0] = it[8]
                    list_t_InstrumentMarginRateUL[1] = it[9]
                elif (it[2] == '1') and (it[3] == '1'):
                    list_t_CurrInstrMarginRate[2] = it[4]
                    list_t_CurrInstrMarginRate[3] = it[5]
                    list_t_CurrExchMarginRate[2] = it[6]
                    list_t_CurrExchMarginRate[3] = it[7]
                    list_t_InstrumentMarginRateUL[2] = it[8]
                    list_t_InstrumentMarginRateUL[3] = it[9]
                elif (it[2] == '3') and (it[3] == '0'):
                    list_t_CurrInstrMarginRate[4] = it[4]
                    list_t_CurrInstrMarginRate[5] = it[5]
                    list_t_CurrExchMarginRate[4] = it[6]
                    list_t_CurrExchMarginRate[5] = it[7]
                    list_t_InstrumentMarginRateUL[4] = it[8]
                    list_t_InstrumentMarginRateUL[5] = it[9]
                elif (it[2] == '3') and (it[3] == '1'):
                    list_t_CurrInstrMarginRate[6] = it[4]
                    list_t_CurrInstrMarginRate[7] = it[5]
                    list_t_CurrExchMarginRate[6] = it[6]
                    list_t_CurrExchMarginRate[7] = it[7]
                    list_t_InstrumentMarginRateUL[6] = it[8]
                    list_t_InstrumentMarginRateUL[7] = it[9]

            li = list_t_CurrInstrMarginRate
            tx = [tradingday, brokerid, 'shfe', 'cu1702', investorRange, 0004, ratioattr, li[0], li[1], li[2], li[3],
                  li[4],
                  li[5], li[6], li[7], 0,
                  'OPN-000+001TRA']
            vi = ''
            for x in tx:
                nc = str(x)
                vi += ',' + '\'' + nc + '\''
            values = '(' + vi.lstrip(',') + ')'

            le = list_t_CurrExchMarginRate
            te = [tradingday, brokerid, 'shfe', 'cu1702', 1, le[0], le[1], le[2], le[3], le[4], le[5], le[6], le[7],
                  'OPN-000+001TRA']
            ve = ''
            for x in te:
                nc = str(x)
                ve += ',' + '\'' + nc + '\''
            values_ex_margin = '(' + ve.lstrip(',') + ')'

            lj = list_t_InstrumentMarginRateUL
            tx = [tradingday, brokerid, 'shfe', 'cu1702', 1, brokerid, 0, lj[0], lj[1], lj[2], lj[3], lj[4], lj[5],
                  lj[6], lj[7]]
            vj = ''
            for x in tx:
                nc = str(x)
                vj += ',' + '\'' + nc + '\''
            values_mar_adj = '(' + vj.lstrip(',') + ')'

            self.con_to_oracle(oracle_host_port, t_currinsmar_name, values)
            self.con_to_oracle(oracle_host_port, t_currexchmar_name, values_ex_margin)
            self.con_to_oracle(oracle_host_port, t_insrmarUL_name, values_mar_adj)

        elif str(context['opts']) == 'CTP1.furatesetting':
            pass
        elif context['opts'] == 'CTP1.opratesetting':
            pass

    def get_response(self, response, context, *args, **kwargs):
        # context['opts']  #CTP1.marginrate
        file_type = self.request.GET.get('export_type')
        response = HttpResponse(
            content_type="%s; charset=UTF-8" % self.export_mimes[file_type])

        file_name = self.opts.verbose_name.replace(' ', '_')
        print context['model_fields']
        print self.export_mimes[file_type]  # output result is asp636 or asp2636
        # response['Content-Disposition'] = ('attachment; filename=%s.%s' % (
        # file_name, file_type)).encode('utf-8')
        response.write(
            getattr(self, 'get_data_export')(context, self.export_mimes[file_type]))

        # View Methods
        # def get_result_list(self, __):
        #     if self.request.GET.get('all', 'off') == 'on':
        #         self.admin_view.list_per_page = sys.maxsize
        #     return __()
        #
        # def result_header(self, item, field_name, row):
        #     item.export = not item.attr or field_name == '__str__' or getattr(item.attr, 'allow_export', True)
        #     return item
        #
        # def result_item(self, item, obj, field_name, row):
        #     item.export = item.field or field_name == '__str__' or getattr(item.attr, 'allow_export', True)
        #     return item


site.register_plugin(ExportToOraMenuPlugin, ListAdminView)
site.register_plugin(Export2oraPlugin, ListAdminView)
