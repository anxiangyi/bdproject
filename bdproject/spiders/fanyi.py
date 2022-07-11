# -*- coding: utf-8 -*-
import scrapy
import json

class BaiduSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com/']

    def start_requests(self):
        urls = ['https://fanyi.baidu.com/sug']
        data = {
            "kw": "word"
        }
        # GET  scrapy.Request(url, callback)
        # POST scrapy.FormRequest(url, formdata, callback)
        for url in urls:
            yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_info)

    def parse_info(self, response):
        json_obj = json.loads(response.text)
        print(json_obj)

