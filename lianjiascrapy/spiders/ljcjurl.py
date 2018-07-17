# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LJcjurlItem

class LJcjurl(scrapy.Spider):
    name = 'ljcjurl'
    allowed_domains = ['bj.ke.com']

    start_urls = []
    # 东城
    # a = 'https://bj.ke.com/chengjiao/dongcheng/pg'
    # for i in range(5, 74):
    #     start_urls.append(a + str(i))
    # 西城
    # a = 'https://bj.ke.com/chengjiao/xicheng/pg'
    # for i in range(7, 91):
    #     start_urls.append(a + str(i) + 'p1p2p3p4p5')
    #     # pg7-pg91
    #     start_urls.append(a + str(i) + 'p1p2p3p4p5')
    # 海淀
    # a = 'https://bj.ke.com/chengjiao/haidian/pg'
    # for i in range(9, 99):
    #     start_urls.append(a + str(i) + 'p6')
    # 朝阳
    # a = 'https://bj.ke.com/chengjiao/chaoyang/pg'
    # for i in range(5, 69):
    #     start_urls.append(a + str(i) + 'p7p8')
    # 石景山
    # a = 'https://bj.ke.com/chengjiao/shijingshan/pg'
    # for i in range(6, 73):
    #     start_urls.append(a + str(i))

    def parse(self, response):
        item = LJcjurlItem()
        for url_item in response.xpath('//ul[@class="listContent"]/li'):
            title = url_item.xpath('.//div[@class="title"]//text()').extract()
            item['title'] = title[0].strip()
            url = url_item.xpath('.//div[@class="title"]/a/@href').extract()
            item['url'] = url[0].strip()
            yield item