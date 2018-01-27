# -*- coding: utf-8 -*-

import json
import scrapy
import requests
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
        if name:
            item['name'] = name[0].strip()
        else:
            item['name'] = unicode('暂无信息', 'utf-8')
        price = response.xpath('//span[@class="xiaoquUnitPrice"]/text()').extract()
        if price:
            item['price'] = price[0].strip()
        else:
            item['price'] = unicode('暂无信息', 'utf-8')
        district = response.xpath('//div[@class="fl l-txt"]/a[3]/text()').extract()
        if district:
            item['district'] = district[0].strip()
        else:
            item['district'] = unicode('暂无信息', 'utf-8')
        region = response.xpath('//div[@class="fl l-txt"]/a[4]/text()').extract()
        if region:
            item['region'] = region[0].strip()
        else:
            item['region'] = unicode('暂无信息', 'utf-8')
        address = response.xpath('//div[@class="xiaoquDetailHeaderContent clear"]/div/div/text()').extract()
        if address:
            item['address'] = address[0].strip()
        else:
            item['address'] = unicode('暂无信息', 'utf-8')
        time = response.xpath('//div[@class="xiaoquInfo"]/div[1]/span[2]/text()').extract()
        if time:
            item['time'] = time[0].strip()
        else:
            item['time'] = unicode('暂无信息', 'utf-8')
        kind = response.xpath('//div[@class="xiaoquInfo"]/div[2]/span[2]/text()').extract()
        if kind:
            item['kind'] = kind[0].strip()
        else:
            item['kind'] = unicode('暂无信息', 'utf-8')
        fee = response.xpath('//div[@class="xiaoquInfo"]/div[3]/span[2]/text()').extract()
        if fee:
            item['fee'] = fee[0].strip()
        else:
            item['fee'] = unicode('暂无信息', 'utf-8')
        wuye = response.xpath('//div[@class="xiaoquInfo"]/div[4]/span[2]/text()').extract()
        if wuye:
            item['wuye'] = wuye[0].strip()
        else:
            item['wuye'] = unicode('暂无消息', 'utf-8')
        product = response.xpath('//div[@class="xiaoquInfo"]/div[5]/span[2]/text()').extract()
        if product:
            item['product'] = product[0].strip()
        else:
            item['product'] = unicode('暂无消息', 'utf-8')
        buildings = response.xpath('//div[@class="xiaoquInfo"]/div[6]/span[2]/text()').extract()
        if buildings:
            item['buildings'] = buildings[0].strip()
        else:
            item['buildings'] = unicode('暂无消息', 'utf-8')
        rooms = response.xpath('//div[@class="xiaoquInfo"]/div[7]/span[2]/text()').extract()
        if rooms:
            item['rooms'] = rooms[0].strip()
        else:
            item['rooms'] = unicode('暂无信息', 'utf-8')
        if address:
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