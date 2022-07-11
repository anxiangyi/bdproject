# -*- coding: utf-8 -*-
import scrapy
import json


class LianjiaSpider(scrapy.Spider):
    name = 'lianjiaershou'
    allowed_domains = ['bj.lianjia.com/ershoufang/']

    start_urls = ["https://bj.lianjia.com/ershoufang/"]

    def parse(self, response):
        a_list = response.xpath('//ul[@class="sellListContent"]/li/div[@class="info clear"]/div[@class="title"]/a')
        for a in a_list:
            href = a.xpath('./@href').extract_first()
            print(len(a_list),href)
            yield scrapy.Request(url=href, callback=self.parse_detail)

    # def start_requests(self):
    #     for page in range(1, 11):
    #         url = "https://bj.lianjia.com/ershoufang/" + "pg{}/".format(page)
    #         yield scrapy.Request(url=url, callback=self.home_parse)

    # def home_parse(self, response):
    #     a_list = response.xpath('//ul[@class="sellListContent"]/li/div[@class="info clear"]/div[@class="title"]/a')
    #     for a in a_list:
    #         # title = a.xpath('./text()').extract_first()
    #         href = a.xpath('./@href').extract_first()
    #         yield scrapy.Request(url=href, callback=self.parse_detail)

    def parse_detail(self, response):
        print("detail_parse:", response.url)
        # name = response.xpath('//div[@class="brokerName"]/a/text()').extract_first()
        # print("name:", name)
