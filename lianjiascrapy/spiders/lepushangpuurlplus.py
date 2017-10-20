# -*- coding: utf-8 -*- 

import time 
from json import dumps, loads
import scrapy
from lianjiascrapy.items import LePuShangPuDetItem


class LePuShangPuDetSpider(scrapy.Spider):
    name = 'lepushangpudetplus'
    allowed_domains = ['lepu.cn']
    
    def start_requests(self):
        start_urls = []
        start_requests = []
        for i in range(1, 787):
            start_urls.append('http://api.lepu.cn/app/shop/search?districts=01-0&page=' + str(i))
        for url in start_urls:
            start_requests.append(scrapy.Request(url))
        return start_requests

    def parse(self, response):
        item = LePuShangPuDetItem()
        text = loads(response.text)
        print(type(text))
        lists = text['data']['info']['list']
        for data in lists:
            id = data['id']
            if id:
                item['id'] = id
            else:
                item['id'] = unicode('暂无信息', "utf-8")
            title = data['ctitle']
            if title: 
                item['title'] = title
            else:
                item['title'] = unicode('暂无信息', "utf-8")
            yield item