# -*- coding: utf-8 -*- 
import json
import scrapy
from lianjiascrapy.items import LJappxiaoquItem

class LJappxiaoqu(scrapy.Spider):
    name = 'ljappxiaoqu'
    allowed_domains = ['app.api.lianjia.com']

    def start_requests(self):
        start_urls = []
        urls = [r'http://app.api.lianjia.com/house/community/search?city_id=110000&district_id=23008614&district_name=%E4%B8%9C%E5%9F%8E&limit_count=20&limit_offset=0']
        start_urls.append(
            scrapy.Request(
                urls[0],
                cookies={
                    'lianjia_uuid': '5454C3DB-7904-462B-A3A7-76092A2C2EF2', 
                    'lianjia_ssid': 'C4950F98-45F5-4C66-ABFA-2DCE36CF0B6D', 
                    'lianjia_udid': 'B8FC5DF1-468F-430D-A29C-B1EB84D46CE6', 
                    'lianjia_token': '2.0013b1eb216a390410021cc2101453c76a'
                }))
        return start_urls

    def parse(self, response):
        item = LJappxiaoquItem()
        item['name'] = 'zr'
        # name = 
        # avg_unit_price = 
        # community_id = 
        yield item