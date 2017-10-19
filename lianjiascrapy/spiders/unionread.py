# -*- coding: utf-8 -*-
import time
import scrapy
from lianjiascrapy.items import YoupuItem

class YoupuSpider(scrapy.Spider):
    name = "unionread"
    allowed_domain = ["unionread.com"]
    start_urls = ["http://unionread.com"]

    def parse(self, response):
        item = YoupuItem()
        for i in range(10000):
            time.sleep(3)
            title = response.xpath('//div[@class="main_left_top"]/text()').extract()
            item['title'] = title[0].strip()
            print(item['title'])