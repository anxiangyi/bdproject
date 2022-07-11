# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 蜘蛛名字， 名字是用来运行程序使用的
    name = 'baidu'

    # 允许的域名，限制爬虫只抓取该域名之下的数据，
    allowed_domains = ['bj.lianjia.com/']

    # 默认spider文件要提交的请求对象的起始url列表
    # scrapy会自动把此列表中的所有url，封装成reqeust对象，提交给引擎
    # start_urls 是scrapy预定的一个变量名，

    # start_urls
    # parse

    # 回调函数
    # 当spider中存在start_urls属性时，scrapy会自动把start_urls列表中的每一个url封装成reqeust对象，通过start_requests函数提交给引擎， scrapy分装的每一个请求，会自动绑定解析回调函数parse
    def start_requests(self):
        urls = ['https://bj.lianjia.com/ershoufang/', 'https://bj.lianjia.com/ershoufang/pg2/']

        request_list = []
        for url in urls:
            # callback要绑定解析函数， 应该保证解析函数和我们提交的url的网页是对应的
            yield scrapy.Request(url=url, callback=self.parse_info)

    # 解析函数，是 一个默认的回调函数，
    def parse_info(self, response):
        print(response.url)
        title_list = response.xpath(
                '//ul[@class="sellListContent"]/li/div[@class="info clear"]/div[@class="title"]/a/text()')

        for title in title_list.extract():
            print(title)
        print('--------------------------------------')

        # 从列表中提取并拆包第一条数据（Selector）
        # 如果解析出来的列表为空，不会报错
        # print(title_list.get())
        # print(title_list.extract_first())

        # print(src.getall())
        # print(src.extract())

        # print(title_list.getall())
        # print(title_list.extract())
        # for title in title_list:
        #     print(title)



        # print(type(response), "----------------------------------------")
        # # HtmlResponse可以直接使用xpath解析，但是解析出的结果是一个Selector对象
        # # Selector对象需要进一步拆包，才能获取到里面的数据
        # src = response.xpath('//div[@id="lg"]/img[1]/@src')
        # print(src.get())
        # print(src.extract_first())

        # print(src.getall())
        # # 使用如下方法解析单个数据和多个数据

        # print(src.extract())

        # //www.baidu.com/img/bd_logo1.png
        # ['//www.baidu.com/img/bd_logo1.png']
        # //www.baidu.com/img/bd_logo1.png
        # ['//www.baidu.com/img/bd_logo1.png']
        # [<Selector xpath='//div[@id="lg"]/img[1]/@src' data='//www.baidu.com/img/bd_logo1.png'>]
