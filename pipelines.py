# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from openpyxl import Workbook  # 写入Excel表所用
from openpyxl import load_workbook

class BjjsPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['证书状态','证书形式','证号','企业名称','法人代表','行政相对人代码','注册地址','经济类型','许可范围',
                       '许可机关','核发日期','前一次有效期','延期有效期'])
    def process_item(self, item, spider):
        line = [item['cert_status'][0],item['cert_medium'][0],item['cert_no'][0],item['corp_name'][0],item['corp_repr'][0],item['admi_code'][0],
                item['regi_addr'][0], item['econ_type'][0], item['prom_rang'][0], item['prom_cell'][0],
                item['chek_date'][0], item['last_chek'][0], item['post_chek'][0]]
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        self.wb.save('D:\\bjjs.xlsx')  # 保存xlsx文件
        return item
