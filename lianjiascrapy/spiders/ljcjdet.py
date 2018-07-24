# -*- coding: utf-8 -*-

import json
import scrapy
from lianjiascrapy.items import LJcjdetItem

class LJcjdet(scrapy.Spider):
    name = 'ljcjdet'
    allowed_domains = ['bj.ke.com']

    def start_requests(self):
        start_urls = []
        urls = []
        with open('xicheng.json', encoding="utf-8") as f:
            for item in f:
                item = json.loads(item)
                urls.append(item['url'])
        for i in range(0, 3750):
            start_urls.append(scrapy.Request(urls[i]))
        return start_urls

    def parse(self, response):
        item = LJcjdetItem()
        item['url'] = response.url
        name = response.xpath('//div[@class="house-title"]//h1/text()').extract()
        if name:
            item['name'] = name[0].strip()
        else:
            item['name'] = '暂无信息'
        date = response.xpath('//div[@class="house-title"]//span/text()').extract()
        if date:
            item['date'] = date[0].split()[0].strip()
        else:
            item['date'] = '暂无信息'
        total_price = response.xpath('//span[@class="dealTotalPrice"]//text()').extract()
        if total_price:
            item['total_price'] = total_price[0].strip()
        else:
            item['total_price'] = '暂无信息'
        unit_price = response.xpath('//div[@class="price"]/b/text()').extract()
        if unit_price:
            item['unit_price'] = unit_price[0].strip()
        else:
            item['unit_price'] = '暂无信息'
        acreage = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract()
        if acreage:
            item['acreage'] = acreage[0].strip()
        else:
            item['acreage'] = '暂无信息'
        period = response.xpath('//div[@class="msg"]/span[2]/label/text()').extract()
        if period:
            item['period'] = period[0].strip()
        else:
            item['period'] = '暂无信息'
        publish_price = response.xpath('//div[@class="msg"]/span[1]/label/text()').extract()
        if publish_price:
            item['publish_price'] = publish_price[0].strip()
        else:
            item['publish_price'] = '暂无信息'
        rooms = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[1]/text()').extract()
        if rooms:
            item['rooms'] = rooms[0].strip()
        else:
            item['rooms'] = '暂无信息'
        floor = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract()
        if floor:
            item['floor'] = floor[0].strip()
        else:
            item['floor'] = '暂无信息'
        fact_acreage = response.xpath('/div[@class="base"]//div[@class="content"]/ul/li[5]/text()').extract()
        if fact_acreage:
            item['fact_acreage'] = fact_acreage[0].strip()
        else:
            item['fact_acreage'] = '暂无信息'
        buildingType = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[6]/text()').extract()
        if buildingType:
            item['buildingType'] = buildingType[0].strip()
        else:
            item['buildingType'] = '暂无信息'
        direction = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[7]/text()').extract()
        if direction:
            item['direction'] = direction[0].strip()
        else:
            item['direction'] = '暂无信息'
        time = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[8]/text()').extract()
        if time:
            item['time'] = time[0].strip()
        else:
            item['time'] = '暂无信息'
        zhuangxiu = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract()
        if zhuangxiu:
            item['zhuangxiu'] = zhuangxiu[0].strip()
        else:
            item['zhuangxiu'] = '暂无信息'
        jianzhujiegou = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[10]/text()').extract()
        if jianzhujiegou:
            item['jianzhujiegou'] = jianzhujiegou[0].strip()
        else:
            item['jianzhujiegou'] = '暂无信息'
        gongnuan = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[11]/text()').extract()
        if gongnuan:
            item['gongnuan'] = gongnuan[0].strip()
        else:
            item['gongnuan'] = '暂无信息'
        tihu = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[12]/text()').extract()
        if tihu:
            item['tihu'] = tihu[0].strip()
        else:
            item['tihu'] = '暂无信息'
        chanquan = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[13]/text()').extract()
        if chanquan:
            item['chanquan'] = chanquan[0].strip()
        else:
            item['chanquan'] = '暂无信息'
        elevator = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[14]/text()').extract()
        if elevator:
            item['elevator'] = elevator[0].strip()
        else:
            item['elevator'] = '暂无信息'
        ljid = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[1]/text()').extract()
        if ljid: 
            item['ljid'] = ljid[0].strip()
        else:
            item['ljid'] = '暂无信息'
        jiaoyiquanshu = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[2]/text()').extract()
        if jiaoyiquanshu:
            item['jiaoyiquanshu'] = jiaoyiquanshu[0].strip()
        else:
            item['jiaoyiquanshu'] = '暂无信息'
        publishtime = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[3]/text()').extract()
        if publishtime:
            item['publishtime'] = publishtime[0].strip()
        else:
            item['publishtime'] = '暂无信息'
        yongtu = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[4]/text()').extract()
        if yongtu:
            item['yongtu'] = yongtu[0].strip()
        else:
            item['yongtu'] = '暂无信息'
        nianxian = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[5]/text()').extract()
        if nianxian:
            item['nianxian'] = nianxian[0].strip()
        else:
            item['nianxian'] = '暂无信息'
        suoshu = response.xpath('//div[@class="transaction"]/div[@class="content"]//li[6]/text()').extract()
        if suoshu:
            item['suoshu'] = suoshu[0].strip()
        else:
            item['suoshu'] = '暂无信息'
        yield item
