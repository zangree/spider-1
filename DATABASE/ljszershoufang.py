# -*- coding: utf-8 -*-

import scrapy
from lianjiascrapy.items import LianjiascrapyItem

class LianjiaSZ(scrapy.Spider):
    name = "szershoufang"
    allowed_domains = ["sz.lianjia.com"]
    start_urls = ["http://sz.lianjia.com/ershoufang/luohu/pg"]

    # basic_urls = "http://sz.lianjia.com/ershoufang/luohu/pg"
    # for page in range(1, 124):
    #     start_urls.append(basic_urls+str(page))

    def parse(self, response):
        item = LianjiascrapyItem()
        for apartment in response.xpath("//li[@class='clear']"):
            title = apartment.xpath(".//div[@class='title']//text()").extract()
            if title:
                item['title'] = title[0].strip()
            else:
                item['title'] = unicode('暂无记录', "utf-8")

            houseInfo = apartment.xpath('.//div[contains(@class, "houseInfo")]//text()').extract()
            if houseInfo:
                item['houseInfo'] = houseInfo[1].strip()
            else:
                item['houseInfo'] = unicode('暂无记录', "utf-8")

            positionInfo = apartment.xpath('.//div[contains(@class, "flood")]//text()').extract()
            if positionInfo:
                item['positionInfo'] = positionInfo[0] + positionInfo[1]
            else:
                item['positionInfo'] = unicode('暂无记录', "utf-8")

            totalPrice = apartment.xpath('.//div[contains(@class, "total")]//text()').extract()
            if totalPrice:
                item['totalPrice'] = totalPrice[0].strip()
            else:
                item['totalPrice'] = unicode('暂无记录', "utf-8")

            unitPrice = apartment.xpath('.//div[contains(@class, "unitPrice")]//text()').extract()
            if unitPrice:
                item['unitPrice'] = unitPrice[0].strip()
            else:
                item['unitPrice'] = unicode('暂无记录', "utf-8")

            region = apartment.xpath('.//div[contains(@class, "address")]//a/text()').extract()
            if region:
                item['region'] = region[0].strip()
            else:
                item['region'] = unicode('暂无记录', "utf-8")
            
            taxfree = apartment.xpath('.//div[contains(@class, "tag")]/span[contains(@class, "taxfree")]/text()').extract()
            if taxfree:
                item['taxfree'] = taxfree[0].strip()
            else:
                item['taxfree'] = unicode('暂无记录', "utf-8")

            haskey = apartment.xpath('.//div[contains(@class, "tag")]/span[contains(@class, "haskey")]/text()').extract()
            if haskey:
                item['haskey'] = haskey[0].strip()
            else:
                item['haskey'] = unicode('暂无记录', "utf-8")
            
            subway = apartment.xpath('.//div[contains(@class, "tag")]/span[contains(@class, "subway")]/text()').extract()
            if subway:
                item['subway'] = subway[0].strip()
            else:
                item['subway'] = unicode('暂无记录', "utf-8")

            yield item