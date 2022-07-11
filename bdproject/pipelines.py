# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

# 负责数据的本地存储，存储之前的逻辑处理
from openpyxl import Workbook


class BdprojectPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['已售出', '材料', '价格'])
        self.file_name = "flower.xlsx"

    # 这是一个回调函数，这个函数负责接收每一个由引擎返回的item对象
    def process_item(self, item, spider):
        print('+++++++++++>>正在写入数据')
        line = [item['sold_num'], item['flower_material'], item['flower_price']]
        self.ws.append(line)
        self.wb.save(self.file_name)
        return item

    def close_spider(self, spider):
        # 关闭
        self.wb.close()
