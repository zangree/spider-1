
# -*- coding: utf-8 -*-

import json
import requests
import scrapy
import requests
from lianjiascrapy.items import FangXiaoQuDetItem


class LianJiaXiaoQuDet(scrapy.Spider):
    name = 'fangxiaoqudet'
    allowed_domains = ['bj.sofang.com']

    def start_requests(self):
        start_urls = []
        with open('fangshan.json') as f:
            for item in f.readlines():
                item = json.loads(item)
                req = scrapy.Request(item['url'])
                start_urls.append(req)
        return start_urls

    def parse(self, response):
        item = FangXiaoQuDetItem()
        name = response.xpath('//div[@class="village_name"]/dl/dt/span[1]/text()').extract()
        if name:
            item['name'] = name[0].strip()
        else:
            item['name'] = unicode('暂无信息', 'utf-8')
        zone = response.xpath('//ul[@class="build_info"]/li[3]/span[2]/text()').extract()
        if zone:
            item['zone'] = zone[0].replace(' ', '').replace('\r\n', '')
        else:
            item['zone'] = unicode('暂无信息', 'utf-8')
        price = response.xpath('//div[@class="village_name"]/dl/dd/p[2]/span[2]/span/text()').extract()
        if price:
            item['price'] = price[0].strip()
        else:
            item['price'] = unicode('暂无信息', 'utf-8')
        address = response.xpath('//ul[@class="build_info"]/li[21]/span[2]/text()').extract()
        if address:
            item['address'] = address[0].strip()
        else:
            item['address'] = unicode('暂无信息', 'utf-8')
        huanxian = response.xpath('//ul[@class="build_info"]/li[5]/span[2]/text()').extract()
        if huanxian:
            item['huanxian'] = huanxian[0].strip()
        else:
            item['huanxian'] = unicode('暂无信息', 'utf-8')
        wuyetype = response.xpath('//ul[@class="build_info"]/li[1]/span[2]/text()').extract()
        if wuyetype:
            item['wuyetype'] = wuyetype[0].strip()
        else:
            item['wuyetype'] = unicode('暂无信息', 'utf-8') 
        product = response.xpath('//ul[@class="build_info"]/li[8]/span[2]/text()').extract()
        if product:
            item['product'] = product[0].strip()
        else:
            item['product'] = unicode('暂无消息', 'utf-8')
        landarea = response.xpath('//ul[@class="build_info"]/li[11]/span[2]/text()').extract()
        if landarea:
            item['landarea'] = landarea[0].strip()
        else:
            item['landarea'] = unicode('暂无信息', 'utf-8') 
        park = response.xpath('//ul[@class="build_info"]/li[19]/span[2]/text()').extract()
        if park:
            item['park'] = park[0].strip()
        else:
            item['park'] = unicode('暂无信息', 'utf-8')
        wuyegongsi = response.xpath('//ul[@class="build_info"]/li[20]/span[2]/text()').extract()
        if wuyegongsi:
            item['wuyegongsi'] = wuyegongsi[0].strip()
        else:
            item['wuyegongsi'] = unicode('暂无信息', 'utf-8')
        fee = response.xpath('//ul[@class="build_info"]/li[15]/span[2]/text()').extract()
        if fee:
            item['fee'] = fee[0].strip()
        else:
            item['fee'] = unicode('暂无信息', 'utf-8')
        code = response.xpath('//ul[@class="build_info"]/li[4]/span[2]/text()').extract()
        if code:
            item['code'] = code[0].strip()
        else:
            item['code'] = unicode('暂无信息', 'utf-8')
        propertydict = response.xpath('//ul[@class="build_info"]/li[6]/span[2]/text()').extract()
        if propertydict:
            item['propertydict'] = propertydict[0].strip()
        else:
            item['propertydict'] = unicode('暂无信息', 'utf-8')
        volume = response.xpath('//ul[@class="build_info"]/li[14]/span[2]/text()').extract()
        if volume:
            item['volume'] = volume[0].strip()
        else:
            item['volume'] = unicode('暂无信息', 'utf-8')
        shape = response.xpath('//ul[@class="build_info"]/li[9]/span[2]/text()').extract()
        if shape:
            item['shape'] = shape[0].strip()
        else:
            item['shape'] = unicode('暂无信息', 'utf-8')
        buildarea = response.xpath('//ul[@class="build_info"]/li[10]/span[2]/text()').extract()
        if buildarea:
            item['buildarea'] = buildarea[0].strip()
        else:
            item['buildarea'] = unicode('暂无信息', 'utf-8')
        rooms = response.xpath('//ul[@class="build_info"]/li[12]/span[2]/text()').extract()
        if rooms:
            item['rooms'] = rooms[0].strip()
        else:
            item['rooms'] = unicode('暂无信息', 'utf-8')
        green = response.xpath('//ul[@class="build_info"]/li[13]/span[2]/text()').extract()
        if green:
            item['green'] = green[0].strip()
        else:
            item['green'] = unicode('暂无信息', 'utf-8')
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
        url = response.xpath('//ul[@class="build_info"]/li[13]/span[2]/text()').extract()
        if url:
            item['url'] = url[0].strip()
        else:
            item['url'] = unicode('暂无信息', 'utf-8')
        yield item