#-*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LJXiaoquDanjiaItem

class LJXiaoquDanjiaSpider(scrapy.Spider):
    name = 'bjxiaoqudanjiaplus'
    allowed_domains = ['bj.lianjia.com']

    def start_requests(self):
        start_urls = []
        start_domains = []
        xiaoqufilename = "ljchaoyangxiaoquurl.txt"
        with open(xiaoqufilename) as f:
            for item in f:
                start_domains.append(item)

        for url in start_domains[:]:
            start_urls.append(scrapy.Request(url.strip()))

        return start_urls

    def parse(self, response):
        item = LJXiaoquDanjiaItem()
        name = response.xpath('//h1[@class="detailTitle"]/text()').extract()
        if name:
            item['title'] = name[0].strip()
        else:
            item['title'] = '暂无信息'
        price = response.xpath('//span[@class="xiaoquUnitPrice"]/text()').extract()
        if price:
            item['price'] = price[0].strip()
        else:
            item['price'] = '暂无信息'
        yield item
