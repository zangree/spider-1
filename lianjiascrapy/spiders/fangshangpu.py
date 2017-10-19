# -*- coding: utf-8 -*-

import sys
import json
import scrapy
from lianjiascrapy.items import XiezilouDetailItem

class XiezilouSpider(scrapy.Spider):
    name = 'xiezilou'
    allowed_domains = ['fang.com/']
    # start_urls = ['http://wangjingsoho.fang.com/xiangqing/']

    # def start_requests(self):
    #     start_urls = []
    #     start =  "http://office.fang.com/loupan/house/i3"
    #     for i in range(1, 81):
    #         url = start + str(i) + '/'
    #         req = scrapy.Request(url)
    #         start_urls.append(req)
    #     return start_urls
    def start_requests(self):
        start_urls = []
        with open("fangxiezilou.json") as f:
            for item in f.readlines():
                item = json.loads(item)
                req = scrapy.Request(item['url']+'xiangqing/')
                start_urls.append(req)
        return start_urls

    def parse(self, response):
        item = XiezilouDetailItem()
        loupanmingcheng = response.xpath('//span[@class="biaoti"]/text()').extract()
        item['loupanmingcheng'] = loupanmingcheng[0].strip() 
        jianjie = response.xpath('//div[@class="firstpic"]//dd/text()').extract()
        item['jianjie'] = jianjie[0].strip() 
        xzlitem = response.xpath('//dl[@class="xiangqing"]')
        suoshuquyu = xzlitem.xpath('./dd[1]/text()').extract()
        item['suoshuquyu'] = suoshuquyu[0].strip()
        loupandizhi = xzlitem.xpath('./dd[2]/span/text()').extract() 
        item['loupandizhi'] = loupandizhi[0].strip()
        huanxianweizhi = xzlitem.xpath('./dd[3]/text()').extract() 
        item['huanxianweizhi'] = huanxianweizhi[0].strip()
        wuyeleixing =  xzlitem.xpath('./dd[4]/text()').extract()
        item['wuyeleixing'] = wuyeleixing[0].strip()
        xieziloudengji = xzlitem.xpath('./dd[5]/text()').extract()
        item['xieziloudengji'] = xieziloudengji[0].strip()
        jianzhuleibie = xzlitem.xpath('./dd[6]/text()').extract()
        item['jianzhuleibie'] = jianzhuleibie[0].strip()
        zongcengshu = xzlitem.xpath('./dd[7]/text()').extract()
        item['zongcengshu'] = zongcengshu[0].strip()
        kaifashang = xzlitem.xpath('./dd[8]/text()').extract()
        item['kaifashang'] = kaifashang[0].strip()
        wuyegongsi = xzlitem.xpath('./dd[12]/text()').extract()
        item['wuyegongsi'] = wuyegongsi[0].strip()
        jungongshijian = xzlitem.xpath('./dd[9]/text()').extract()
        item['jungongshijian'] = jungongshijian[0].strip()
        defanglv = xzlitem.xpath('./dd[10]/text()').extract()
        item['defanglv'] = defanglv[0].strip()
        wuyefei = xzlitem.xpath('./dd[11]/text()').extract()
        item['wuyefei'] = wuyefei[0].strip()
        zhandimianji = xzlitem.xpath('./dd[13]/text()').extract()
        item['zhandimianji'] = zhandimianji[0].strip()
        jianzhumianji = xzlitem.xpath('./dd[14]/text()').extract()
        item['jianzhumianji'] = jianzhumianji[0].strip()
        kaijianmianji = xzlitem.xpath('./dd[15]/text()').extract()
        item['kaijianmianji'] = kaijianmianji[0].strip()
        shifoukefenge = xzlitem.xpath('./dd[16]/text()').extract()
        item['shifoukefenge'] = shifoukefenge[0].strip()
        shifoushewai = xzlitem.xpath('./dd[17]/text()').extract()
        item['shifoushewai'] = shifoushewai[0].strip()
        diantishuliang = xzlitem.xpath('./dd[18]/text()').extract()
        item['diantishuliang'] = diantishuliang[0].strip()
        kongtiaoleixing = xzlitem.xpath('./dd[19]/text()').extract()
        item['kongtiaoleixing'] = kongtiaoleixing[0].strip()
        zhuangxiuzhuangkuang = xzlitem.xpath('./dd[20]/text()').extract()
        item['zhuangxiuzhuangkuang'] = zhuangxiuzhuangkuang[0].strip()
        tingchewei = xzlitem.xpath('./dd[21]/text()').extract()
        item['tingchewei'] = tingchewei[0].strip()
        louneipeitao = xzlitem.xpath('./dt[1]/text()').extract()
        item['louneipeitao'] = louneipeitao[0].strip()
        yield item
