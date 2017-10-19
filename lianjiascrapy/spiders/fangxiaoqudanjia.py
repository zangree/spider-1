#-*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import FangXiaoQuDanJiaItem

class FangXiaoQuDanJiaSpider(scrapy.Spider):
    name = 'fangxiaoqudanjia'
    allow_domians = ['esf.fang.com']

    def start_requests(self):
        start_urls = []
        start_domians = [
            # ('http://esf.fang.com/housing/1__1_0_0_0_', 64) # chaoyang
            # ,
            # ('http://esf.fang.com/housing/0__1_0_0_0_', 64) # haidian
            # ,
            # ('http://esf.fang.com/housing/6__1_0_0_0_', 44) # fengtai
            # ,
            # ( 'http://esf.fang.com/housing/2__1_0_0_0_', 33) # dongcheng
            # ,
            # ('http://esf.fang.com/housing/3__1_0_0_0_', 52) # xicheng
            # ,
            ('http://esf.fang.com/housing/7__1_0_0_0_', 10) # shijingshan
        ]
        for item, pages in start_domians:
            for i in range(1, pages):
                url = item + str(i) + '_0_0/'
                start_urls.append(scrapy.Request(url))
        return start_urls

    def parse(self, response):
        item = FangXiaoQuDanJiaItem()
        for dj_item in response.xpath('//div[@class="houseList"]/div[@class="list rel"]'):
            title = dj_item.xpath('.//dd[1]/p/a/text()').extract()
            if title:
                item['title'] = title[0].strip()
            else:
                item['title'] = unicode('暂无信息', 'utf-8')
            price = dj_item.xpath('./div[@class="listRiconwrap"]/p[1]/span[1]/text()').extract()
            if price:
                item['price'] = price[0].strip()
            else:
                item['price'] = unicode('暂无信息', 'utf-8')
            yield item
