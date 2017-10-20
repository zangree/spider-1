#-*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LJcjItem

class LJcj(scrapy.Spider):
    name = 'bjxiaoqucj'
    allowed_domains = ['bj.lianjia.com']

    start_urls = []
    a = "http://bj.lianjia.com/chengjiao/fengtai/pg"
    for i in range(1, 13):
        start_urls.append(a+str(i)+'p1p2')

    # def start_requests(self):
    #     a = 'http://bj.lianjia.com/chengjiao/'
    #     start_urls = []
    #     with open('ljdongchengcj.txt') as f:
    #         for item in f.readlines():
    #             print(item)
    #             for i in range(1, 11):
    #                 # 从“小区”进入
    #                 # itempg = a + str(i) + item.split('/')[4].strip()
    #                 # 从“成交”进入
    #                 itempg = a + item.split('/')[4].strip() + '/pg' + str(i)
    #                 req = scrapy.Request(itempg)
    #                 start_urls.append(req)
    #     return start_urls                


    def parse(self, response):
        item = LJcjItem()
        for cj_item in response.xpath('//div[@class="content"]//ul[@class="listContent"]/li'):
            title = cj_item.xpath('.//div[@class="title"]//text()').extract()
            print(title)
            item['title'] = title[0].strip()
            # '2017.03.31'
            dealDate = cj_item.xpath('.//div[@class="dealDate"]//text()').extract()
            item['dealDate'] = dealDate[0].strip()
            
            totalPrice = cj_item.xpath('.//div[@class="totalPrice"]//text()').extract()
            item['totalPrice'] = totalPrice[0].strip()
            # 
            unitPrice = cj_item.xpath('.//div[@class="unitPrice"]//text()').extract()
            item['unitPrice'] = unitPrice[0].strip()
            # 南 北 | 简装 | 有电梯
            houseInfo = cj_item.xpath('.//div[@class="houseInfo"]//text()').extract()
            item['houseInfo'] = houseInfo[0].strip()
            # 底层(共19层) 2006年建板塔结合
            positionInfo = cj_item.xpath('.//div[@class="positionInfo"]//text()').extract()
            item['positionInfo'] = positionInfo[0].strip()
            yield item