# -*- coding: utf-8 -*-

import json
import requests
import scrapy
from lianjiascrapy.items import LianJiaXiaoQuDetItem

class LianJiaXiaoQuDet(scrapy.Spider):
    name = 'ljxiaoqudet'
    allowed_domains = ['bj.lianjia.com']

    def start_requests(self):
        start_urls = []
        with open('fangshan.json') as f:
            for item in f.readlines():
                item = json.loads(item)
                req = scrapy.Request(item['url'])
                start_urls.append(req)
        return start_urls

    def parse(self, response):
        item = LianJiaXiaoQuDetItem()
        name = response.xpath('//h1[@class="detailTitle"]/text()').extract()
        item['name'] = name[0].strip()
        price = response.xpath('//span[@class="xiaoquUnitPrice"]/text()').extract()
        item['price'] = price[0].strip()
        district = response.xpath('//div[@class="fl l-txt"]/a[3]/text()').extract()
        item['district'] = district[0].strip()
        region = response.xpath('//div[@class="fl l-txt"]/a[4]/text()').extract()
        item['region'] = region[0].strip()
        address = response.xpath('//div[@class="xiaoquDetailHeaderContent clear"]/div/div/text()').extract()
        item['address'] = address[0].strip()
        time = response.xpath('//div[@class="xiaoquInfo"]/div[1]/span[2]/text()').extract()
        item['time'] = time[0].strip()
        kind = response.xpath('//div[@class="xiaoquInfo"]/div[2]/span[2]/text()').extract()
        item['kind'] = kind[0].strip()
        fee = response.xpath('//div[@class="xiaoquInfo"]/div[3]/span[2]/text()').extract()
        item['fee'] = fee[0].strip()
        wuye = response.xpath('//div[@class="xiaoquInfo"]/div[4]/span[2]/text()').extract()
        item['wuye'] = wuye[0].strip()
        product = response.xpath('//div[@class="xiaoquInfo"]/div[5]/span[2]/text()').extract()
        item['product'] = product[0].strip()
        buildings = response.xpath('//div[@class="xiaoquInfo"]/div[6]/span[2]/text()').extract()
        item['buildings'] = buildings[0].strip()
        rooms = response.xpath('//div[@class="xiaoquInfo"]/div[7]/span[2]/text()').extract()
        item['rooms'] = rooms[0].strip()
        location_str = 'https://api.map.baidu.com/geocoder/v2/?address=' + item['address'].split(' ')[0] + '&output=json&ak=39GuXLCBZK4Tk7wxdtUZ5NqPbOK1iRRG'
        location = requests.get(location_str).json()
        if location['status'] == 0:
            lng = location['result']['location']['lng']
            if lng:
                item['lng'] = lng
            else:
                item['lng'] = unicode('暂无信息', 'utf-8')
            lat = location['result']['location']['lat']
            if lat:
                item['lat'] = lat
            else:
                item['lat'] = unicode('暂无信息', 'utf-8')
        else:
            item['lng'] = unicode('暂无信息', 'utf-8')
            item['lat'] = unicode('暂无信息', 'utf-8')
        yield item