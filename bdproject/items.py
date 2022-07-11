# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 描述数据格式的一个文件，这里封装一个类，表示要爬取的数据的字段
class BdprojectItem(scrapy.Item):
    # 声明爬虫希望保留的字段，但是并不是强制语法，所以不写也不会报错，但是为了scrapy的完整逻辑，建议声明
    # scrapy.Item本质就是一个dict对象，所以我们可以用字典来代替Item对象的声明
    sold_num = scrapy.Field()
    flower_material = scrapy.Field()
    flower_price = scrapy.Field()
