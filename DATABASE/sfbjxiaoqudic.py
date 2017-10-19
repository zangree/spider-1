# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import SFbjxiaoquItem

class SFbjxiaoquDic(scrapy.Spider):
    name = 'sfbjxiaoqudic'
    allowed_domains = ['bj.sofang.com']
    start_urls = []
    basic_urls = ['http://bj.sofang.com/saleesb/area/aa7-bl']
    # basic_urls = [
    #     'http://bj.sofang.com/saleesb/area/aa1-bl',     # 东城
    #     'http://bj.sofang.com/saleesb/area/aa2-bl',     # 西城
    #     'http://bj.sofang.com/saleesb/area/aa5-bl',     # 朝阳
    #     'http://bj.sofang.com/saleesb/area/aa8-bl',     # 海淀
    #     'http://bj.sofang.com/saleesb/area/aa6-bl',     # 丰台
    #     'http://bj.sofang.com/saleesb/area/aa7-bl'      # 石景山
    # ]
    # XQxuhao = int(raw_input("xiaoqu seq num: "))
    pages = int(raw_input("input total pages: "))
    for page in range(1, pages+1):
        start_urls.append(basic_urls[0]+str(page))
    
    def parse(self, response):
        item = SFbjxiaoquItem()
        i = 0
        for xiaoqu in response.xpath('//div[@class="build_list"]/dl'):
            i += 1
            sfbjxq_name = xiaoqu.xpath('.//a[@class="name build_width"]/text()').extract()
            print(i)
            if sfbjxq_name:
                item['sfbjxq_name'] = sfbjxq_name[0].strip()
            else:
                item['sfbjxq_name'] = unicode('暂无记录', 'utf-8')

            sfbjxq_url = xiaoqu.xpath('.//a[@class="name build_width"]/@href').extract()
            if sfbjxq_url:
                item['sfbjxq_url'] = sfbjxq_url[0].strip()
            else:
                item['sfbjxq_url'] = unicode('暂无记录', 'utf-8')

            sfbjxq_price = xiaoqu.xpath('.//span[@class="colorfe fontA"]/text()').extract()
            if sfbjxq_price:
                item['sfbjxq_price'] = sfbjxq_price[0].strip()
            else:
                item['sfbjxq_price'] = unicode('暂无记录', 'utf-8')
            
            yield item
                 