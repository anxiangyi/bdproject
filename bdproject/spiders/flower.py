import scrapy

from scrapy_redis.spiders import RedisSpider
from bdproject.items import BdprojectItem


class FlowerSpider(scrapy.Spider):
    name = "flower"
    allowed_domains = ['http://www.maihua.me/']

    def start_requests(self):
        url = "http://www.maihua.me/research2-1.html"
        yield scrapy.Request(url=url, callback=self.parse_info)

    def parse_info(self, response):
        flower_xpath = response.xpath("//div//li[@class='goodsItem']")
        sold_num_list = flower_xpath.xpath("./p/strong/font")
        for i in range(1, len(sold_num_list) + 1):
            sold_num = sold_num_list[i - 1].xpath("./text()").extract_first()
            path = "//div//li[@class='goodsItem'][{}]".format(i) + "/p/a/@href"
            href = 'http://www.maihua.me/' + response.xpath(path)[1].get()
            yield scrapy.Request(url=href, callback=self.parse_s, meta={"sold_num": sold_num}, dont_filter=True)

    def parse_s(self, response):
        item = BdprojectItem()
        sold_num = response.meta["sold_num"]
        flower_material = response.xpath("//div/div[@class='clearfix']//tr[1]/td[2]/text()").get()
        flower_price = response.xpath("//font[@id='ECS_SHOPPRICE']/cite/text()").get()
        print("+++++++++++", sold_num, flower_material, flower_price)
        item["sold_num"] = sold_num
        item["flower_material"] = flower_material
        item["flower_price"] = flower_price
        yield item
