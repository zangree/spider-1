# -*- coding: utf-8 -*-
import time
import scrapy
from lianjiascrapy.items import YoupuItem

class YoupuSpider(scrapy.Spider):
    name = "youpu"
    allowed_domain = ["urplus.cn"]
    start_urls = ["http://urplus.cn"]

    def parse(self, response):
        item = YoupuItem()
        for i in range(10000):
            time.sleep(3)
            title = response.xpath('//div[@class="title"]/text()').extract()
            item['title'] = title[0].strip()
            yield item