#-*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LJXiaoquDanjiaItem

class LJXiaoquDanjiaSpider(scrapy.Spider):
    name = 'bjxiaoqudanjia'
    allowed_domains = ['bj.lianjia.com']

    def start_requests(self):
        start_urls = []
        start_domains = [
            # ('http://bj.lianjia.com/xiaoqu/dongcheng/', 39)
            # ,
            #  ('http://bj.lianjia.com/xiaoqu/xicheng/', 54)
            # ,
            # ('http://bj.lianjia.com/xiaoqu/chaoyang/', 59)
            # ,
            # ('http://bj.lianjia.com/xiaoqu/haidian/', 56)
            # ,
            # ('http://bj.lianjia.com/xiaoqu/fengtai/', 40)
            # ,
            #('http://bj.lianjia.com/xiaoqu/shijingshan/', 9)
            # ,
            #('http://bj.lianjia.com/xiaoqu/tongzhou/', 23)
            # ,
            #('http://bj.lianjia.com/xiaoqu/changping/', 27)
            # ,
            #('http://bj.lianjia.com/xiaoqu/daxing/', 27)
            # ,
            #('http://bj.lianjia.com/xiaoqu/yizhuangkaifaqu/', 5)
            # ,
            #('http://bj.lianjia.com/xiaoqu/shunyi/', 12)
            # ,
            #('http://bj.lianjia.com/xiaoqu/fangshan/', 20)
            # ,
            #('http://bj.lianjia.com/xiaoqu/mentougou/', 8)
            # ,
            #('http://bj.lianjia.com/xiaoqu/pinggu/', 2)
            # ,
            #('http://bj.lianjia.com/xiaoqu/huairou/', 4)
            # ,
            #('http://bj.lianjia.com/xiaoqu/miyun/', 5)
        ]
        for item, pages in start_domains:
            for i in range(1, pages):
                url = item + 'pg' + str(i)
                start_urls.append(scrapy.Request(url))
        return start_urls

    def parse(self, response):
        item = LJXiaoquDanjiaItem()
        for dj_item in response.xpath('//div[@class="content"]//ul[@class="listContent"]/li'):
            name = dj_item.xpath('.//div[@class="title"]//text()').extract()
            print(name)
            item['title'] = name[1].strip()
            danjia = dj_item.xpath('.//div[@class="totalPrice"]/span/text()').extract()
            item['price'] = danjia[0].strip()
            yield item
