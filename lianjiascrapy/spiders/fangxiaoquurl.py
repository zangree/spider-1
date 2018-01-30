# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import FangXiaoQuURLItem

class LianJiaXiaoQuUrl(scrapy.Spider):
    name = 'fangxiaoquurl'
    allowed_domains = ['bj.sofang.com']

    def start_requests(self):
        start_urls = []
        start_domains = [
            ('http://bj.sofang.com/saleesb/area/aa10', 23),
        ]
        for item, pages in start_domains:
            for i in range(1, pages):
                url = item + '-bl' + str(i) + '?'
                start_urls.append(scrapy.Request(url))
        return start_urls

    def parse(self, response):
        item = FangXiaoQuURLItem()
        for xiaoqu in response.xpath('//div[@class="list list_free xinfang"]/dl'):
            url = xiaoqu.xpath('.//dd[@class="house_msg"]//a/@href').extract()
            item['url'] = 'http://bj.sofang.com' + url[0].strip().replace('esfindex', 'esfbd')
            name = xiaoqu.xpath('.//dd[@class="house_msg"]//a/text()').extract()
            item['name'] = name[0].strip()
            yield item