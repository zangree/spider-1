# -*- coding: utf-8 -*- 

import scrapy
from lianjiascrapy.items import FangShangPuURL

class FangShangPuURLSpider(scrapy.Spider):
    name = 'fangshangpuurl'
    allowed_domains = ['fang.com/']
    start_urls = [
        'http://shop.fang.com/loupan/house-a01/j340/',
        'http://shop.fang.com/loupan/house-a01/i32-j340/',
        'http://shop.fang.com/loupan/house-a01/i33-j340/',
        'http://shop.fang.com/loupan/house-a01/i34-j340/',
        'http://shop.fang.com/loupan/house-a01/i35-j340/',
        'http://shop.fang.com/loupan/house-a01/i36-j340/',
        'http://shop.fang.com/loupan/house-a01/i37-j340/',
        'http://shop.fang.com/loupan/house-a01/i38-j340/',
        'http://shop.fang.com/loupan/house-a01/i39-j340/',
        'http://shop.fang.com/loupan/house-a01/i310-j340/',
        'http://shop.fang.com/loupan/house-a01/i311-j340/',
        ]
    
    def parse(self, response):
        item = FangShangPuURL()
        for one in response.xpath('//div[@class="houseList"]/dl'):
            shangpu = one.xpath('.//p[@class="title"]/a/text()').extract()
            item['shangpu'] = shangpu[0].strip()
            url = one.xpath('.//p[@class="title"]/a/@href').extract()
            item['url'] = url[0].strip()
            yield item