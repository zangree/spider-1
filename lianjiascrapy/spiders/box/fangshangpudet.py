# -*- coding: utf-8 -*-

import json
import scrapy
from lianjiascrapy.items import FangShangPuDetItem

class FangShangPuDetSpider(scrapy.Spider):
    name = 'fangshangpudet'
    allowed_domains = ['fang.com/']
    
    def start_requests(self):
        start_urls = []
        with open('fangshangpuurl.json') as f:
            for item in f.readlines():
                item = json.loads(item)
                req = scrapy.Request(item['url']+'xiangqing/')
                start_urls.append(req)
        return start_urls

    def parse(self, response):
        item = FangShangPuDetItem()
        shangpu = response.xpath('//span[@class="biaoti"]/text()').extract()
        item['shangpu'] = shangpu[0].strip()
        shangpuitem = response.xpath('//dl[@class="xiangqing"]')
        quyu = shangpuitem.xpath('./dd[1]/text()').extract()
        item['quyu'] = quyu[0].strip()
        dizhi = shangpuitem.xpath('./dd[2]/span/text()').extract()
        item['dizhi'] = dizhi[0].strip()
        huanxianweizhi = shangpuitem.xpath('./dd[3]/text()').extract()
        item['huanxianweizhi'] = huanxianweizhi[0].strip()
        wuyeleibie = shangpuitem.xpath('./dd[4]/text()').extract()
        item['wuyeleibie'] = wuyeleibie[0].strip()
        jianzhuleibie = shangpuitem.xpath('./dd[5]/text()').extract()
        item['jianzhuleibie'] = jianzhuleibie[0].strip()
        zongcengshu = shangpuitem.xpath('./dd[6]/text()').extract()
        item['zongcengshu'] = zongcengshu[0].strip()
        kaifashang = shangpuitem.xpath('./dd[7]/text()').extract()
        item['kaifashang'] = kaifashang[0].strip()
        jungongshijian = shangpuitem.xpath('./dd[8]/text()').extract()
        item['jungongshijian'] = jungongshijian[0].strip()
        wuyefei = shangpuitem.xpath('./dd[9]/text()').extract()
        item['wuyefei'] = wuyefei[0].strip()
        wuyegongsi = shangpuitem.xpath('./dd[10]/text()').extract()
        item['wuyegongsi'] = wuyegongsi[0].strip()
        zhandimianji = shangpuitem.xpath('./dd[11]/text()').extract()
        item['zhandimianji'] = zhandimianji[0].strip()
        jianzhumianji = shangpuitem.xpath('./dd[12]/text()').extract()
        item['jianzhumianji'] = jianzhumianji[0].strip()
        shifoukefenge = shangpuitem.xpath('./dd[14]/text()').extract()
        item['shifoukefenge'] = shifoukefenge[0].strip()
        diantishuliang = shangpuitem.xpath('./dd[15]/text()').extract()
        item['diantishuliang'] = diantishuliang[0].strip()
        zhuangxiuzhuangkuang = shangpuitem.xpath('./dd[17]/text()').extract()
        item['zhuangxiuzhuangkuang'] = zhuangxiuzhuangkuang[0].strip()
        tingchewei = shangpuitem.xpath('./dd[18]/text()').extract()
        item['tingchewei'] = tingchewei[0].strip()
        yield item