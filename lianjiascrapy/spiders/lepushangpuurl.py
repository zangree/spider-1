# -*- coding: utf-8 -*- 

import scrapy
from lianjiascrapy.items import  LePuShangPuURLItem

class LePuShangPuURLSpider(scrapy.Spider):
    """
    
    """
    name = 'lepushangpuurl'
    allowed_domains = ['lepu.cn']
    
    def start_requests(self):
        start_urls = []
        for i in range(42):
            url_item = "http://www.lepu.cn/shop/shijingshan/p" + str(i+1)
            start_urls.append(scrapy.Request(url_item))
        return start_urls

    def parse(self, response):
        item = LePuShangPuURLItem()
        for one in response.xpath('//div[@class="pusource_box"]/ul[@class="pu_bot"]/li[@class="clearfix"]'):
            shangpu = one.xpath('.//div[@class="arrive"]/h2/a/text()').extract()
            item['shangpu'] = shangpu[0].strip()
            url = one.xpath('.//div[@class="arrive"]/h2/a/@href').extract()
            item['url'] = url[0].strip()
            yield item