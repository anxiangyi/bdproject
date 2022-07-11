# -*- coding: utf-8 -*-
import scrapy
import json


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com/']

    def start_requests(self):
        urls = ["https://bj.lianjia.com/ershoufang/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_info)

    # 不要做任何和解析无关的事
    # 必须要返回一个可迭代对象（reqeust, item）
    def parse_info(self, response):
        title_list = response.xpath(
                '//ul[@class="sellListContent"]/li/div[@class="info clear"]/div[@class="title"]/a/text()')
        for title in title_list.extract():
            # scrapy中，数据的描述可以直接使用字典来替代
            # 实际上是返回了一个Item对象
            yield {"title": title}
