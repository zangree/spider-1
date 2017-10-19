# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LJbjxiaoquItem

class LJbjxiaoquDic(scrapy.Spider):
    name = "bjxiaoqudic"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = []
    basic_urls = [
        "http://bj.lianjia.com/xiaoqu/dongcheng/pg",
        "http://bj.lianjia.com/xiaoqu/xicheng/pg",
        "http://bj.lianjia.com/xiaoqu/chaoyang/pg",
        "http://bj.lianjia.com/xiaoqu/haidian/pg",
        "http://bj.lianjia.com/xiaoqu/fengtai/pg",
        "http://bj.lianjia.com/xiaoqu/shijingshan/pg",
        "http://bj.lianjia.com/xiaoqu/tongzhou/pg"
        ]
    XQxuhao = int(raw_input("xiaoqu seq num: "))
    pages = int(raw_input("input pages: "))
    for page in range(1, pages+1):
        start_urls.append(basic_urls[XQxuhao]+str(page))
    '''
        "http://bj.lianjia.com/xiaoqu/xicheng/",
        "http://bj.lianjia.com/xiaoqu/chaoyang/",
        "http://bj.lianjia.com/xiaoqu/haidian/",
        "http://bj.lianjia.com/xiaoqu/fengtai/",
        "http://bj.lianjia.com/xiaoqu/shijingshan/",
        "http://bj.lianjia.com/xiaoqu/tongzhou/"
        ]
    '''
    def parse(self, response):
        item = LJbjxiaoquItem()
        for xiaoqu in response.xpath('//li[@class="clear xiaoquListItem"]'):
            bjxiaoqu_name = xiaoqu.xpath('.//div[@class="title"]//text()').extract() 
            print(bjxiaoqu_name)
            if bjxiaoqu_name:
                item['bjxiaoqu_name'] = bjxiaoqu_name[1].strip()
            else:
                item['bjxiaoqu_name'] = unicode('暂无记录', "utf-8")

            bjxiaoqu_url = xiaoqu.xpath('.//div[@class="title"]//@href').extract()
            if bjxiaoqu_url:
                item['bjxiaoqu_url'] = bjxiaoqu_url[0].strip()
            else:
                item['bjxiaoqu_url'] = unicode('暂无记录', "utf-8")

            bjxiaoqu_price = xiaoqu.xpath('.//div[@class="totalPrice"]//text()').extract() 
            if bjxiaoqu_price:
                item['bjxiaoqu_price'] = bjxiaoqu_price[0].strip()
            else:
                item['bjxiaoqu_price'] = unicode('暂无记录', "utf-8")
            
            yield item