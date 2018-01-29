# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LianJiaXiaoQuURLItem

class LianJiaXiaoQuUrl(scrapy.Spider):
    name = 'ljxiaoquurl'
    allowed_domains = ['bj.lianjia.com']

    def start_requests(self):
        start_urls = []
        start_domains = [
            ('http://bj.sofang.com/saleesb/area/aa10', 23),
            # ('https://bj.lianjia.com/xiaoqu/tongzhou/', 22),
            # ('https://bj.lianjia.com/xiaoqu/changping/', 27),
            # ('https://bj.lianjia.com/xiaoqu/daxing/', 16),
            # ('https://bj.lianjia.com/xiaoqu/yizhuangkaifaqu/', 5),
            # ('https://bj.lianjia.com/xiaoqu/shunyi/', 12),
            # ('https://bj.lianjia.com/xiaoqu/mentougou/', 8),
            # ('https://bj.lianjia.com/xiaoqu/miyun/', 5)
        ]
        for item, pages in start_domains:
            for i in range(1, pages):
                url = item + 'pg' + str(i)
                start_urls.append(scrapy.Request(url))
        return start_urls

    def parse(self, response):
        item = LianJiaXiaoQuURLItem()
        for xiaoqu in response.xpath('//ul[@class="listContent"]/li'):
            url = xiaoqu.xpath('.//div[@class="title"]/a/@href').extract()
            print(url)
            item['url'] = url[0].strip()
            name = xiaoqu.xpath('.//div[@class="title"]/a/text()').extract()
            item['name'] = name[0].strip()
            yield item