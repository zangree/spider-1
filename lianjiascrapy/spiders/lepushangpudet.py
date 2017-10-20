# -*- coding: utf-8 -*- 

import time
import json
import scrapy
from lianjiascrapy.items import  LePuShangPuDetItem


class LePuShangPuDetSpider(scrapy.Spider):
    name = 'lepushangpudet'
    allowed_domains = ['lepu.cn']
    # start_urls = ['http://www.lepu.cn/shop/detail-408326/']
    def start_requests(self):
        start_urls = []
        ids = []
        with open('chaoyangid.json') as f:
            for item in f:
                item = json.loads(item)
                ids.append(item['id'])
        print(len(ids))
        for i in range(2000, 2421):
            start_urls.append(scrapy.Request("http://www.lepu.cn/shop/detail-"+str(ids[i])))
        return start_urls

    def parse(self, response):
        item = LePuShangPuDetItem()
        title = response.xpath('//div[@class="lp_top"]//div[@class="title-left"]/h1/text()').extract()
        if title:
            item['title'] = title[0].strip()
        else:
            item['title'] = unicode('暂无信息', "utf-8")
        id = response.xpath('//div[@class="house_info"]/h2/span[1]/text()').extract()
        if id:
            item['id'] = id[0].strip()
        else:
            item['id'] = unicode('暂无信息', "utf-8")
        update = response.xpath('//div[@class="house_info"]/h2/span[2]/text()').extract()
        if update:
            item['update'] = update[0].strip()
        else:
            item['update'] = unicode('暂无信息', "utf-8")
        area =  response.xpath('//div[@class="top-content"]//div[@class="det-text"]/ul[@class="details f16"]/li[2]//span/text()').extract()
        if area:
            item['area'] = area[0].strip()
        else:
            item['area'] = unicode('暂无信息', "utf-8")
        month = response.xpath('//div[@class="top-content"]//div[@class="det-text"]//ul[@class="bt3 clearfix"]/li[2]/span[1]/b/text()').extract()
        if month:
            item['month'] = month[0].strip()
        else:
            item['month'] = unicode('暂无信息', "utf-8")
        day = response.xpath('//div[@class="top-content"]//div[@class="det-text"]//ul[@class="bt3 clearfix"]/li[2]/span[1]/i/text()').extract()
        if day:
            item['day'] = day[0].strip()
        else:
            item['day'] = unicode('暂无信息', "utf-8")
        transfer = response.xpath('//div[@class="top-content"]//div[@class="det-text"]//ul[@class="bt3 clearfix"]/li[3]/span/b/text()').extract()
        if transfer:
            item['transfer'] = transfer[0].strip()
        else:
            item['transfer'] = unicode('暂无信息', 'utf-8')
        tag1 = response.xpath('//div[@class="top-content"]//div[@class="det-text"]//div[@class="flag_div"]/span[1]/text()').extract()
        if tag1:
            item['tag1'] = tag1[0].strip()
        else:
            item['tag1'] = unicode('暂无信息', 'utf-8')
        tag2 = response.xpath('//div[@class="top-content"]//div[@class="det-text"]/ul[@class="details f16"]//div[@class="flag_div"]/span[2]/text()').extract()
        if tag2:
            item['tag2'] = tag2[0].strip()
        else:
            item['tag2'] = unicode('暂无信息', 'utf-8')
        tag3 = response.xpath('//div[@class="top-content"]//div[@class="det-text"]//div[@class="flag_div"]/span[3]/text()').extract()
        if tag3:
            item['tag3'] = tag3[0].strip()
        else:
            item['tag3'] = unicode('暂无信息', 'utf-8')
        region = response.xpath('//div[@class="top-content"]//div[@class="det-text"]/ul[@class="details f16"]/li[2]/p[1]/span/text()').extract()
        if region:
            item['region'] = region[0].strip()
        else:
            item['region'] = unicode('暂无信息', "utf-8")
        address = response.xpath('//div[@class="top-content"]//div[@class="det-text"]/ul[@class="details f16"]/li[3]/p/span/text()').extract()
        if address:
            item['address'] = address[0].strip()
        else:
            item['address'] = unicode('暂无信息', "utf-8")
        running = response.xpath('//div[@class="detail_info"]/div[@class="puyuan_info"]/ul/li[1]/div[@class="tips-info"]/p[1]/span/b/text()').extract()
        if running:
            item['running'] = running[0].strip()
        else:
            item['running'] = unicode('暂无信息', "utf-8")
        license = response.xpath('//div[@class="detail_info"]/div[@class="puyuan_info"]/ul/li[1]/div[@class="tips-info"]/p[2]/span[1]/b/text()').extract()
        if license:
            item['license'] = license[0].strip()
        else:
            item['license'] = unicode('暂无信息', "utf-8")
        shoptype = response.xpath('//div[@class="puyuan_info"]/ul/li[2]/div[@class="tips-info fl"]/p[1]/span[1]/b/text()').extract()
        if shoptype:
            item['shoptype'] = shoptype[0].strip()
        else:
            item['shoptype'] = unicode('暂无信息', "utf-8")
        floor = response.xpath('//div[@class="puyuan_info"]/ul/li[2]/div[@class="tips-info fl"]/p[1]/span[3]/b/text()').extract()
        if floor:
            item['floor'] = floor[0].strip()
        else:
            item['floor'] = unicode('暂无信息', "utf-8")
        width = response.xpath('//div[@class="puyuan_info"]/ul/li[2]/div[@class="tips-info fl"]/p[2]/span[1]/b/text()').extract()
        if width:
            item['width'] = width[0].strip()
        else:
            item['width'] = unicode('暂无信息', "utf-8")
        depth = response.xpath('//div[@class="puyuan_info"]/ul/li[2]/div[@class="tips-info fl"]/p[2]/span[2]/b/text()').extract()
        if depth:
            item['depth'] = depth[0].strip()
        else:
            item['depth'] = unicode('暂无信息', "utf-8")
        height = response.xpath('//div[@class="puyuan_info"]/ul/li[2]/div[@class="tips-info fl"]/p[2]/span[3]/b/text()').extract()
        if height:
            item['height'] = height[0].strip()
        else:
            item['height'] = unicode('暂无信息', "utf-8")
        ring = response.xpath('//div[@class="puyuan_info"]/ul/li[3]/div[@class="tips-info fl"]/p[1]/span[2]/b/text()').extract()
        if ring:
            item['ring'] = ring[0].strip()
        else:
            item['ring'] = unicode('暂无信息', "utf-8")
        street = response.xpath('//div[@class="puyuan_info"]/ul/li[3]/div[@class="tips-info fl"]/p[1]/span[3]/b/text()').extract()
        if street:
            item['street'] = street[0].strip()
        else:
            item['street'] = unicode('暂无信息', "utf-8")
        payment = response.xpath('//div[@class="feiyong_dec"]/ul/li/div[@class="tips-info"]/p[1]/span[2]/b/text()').extract()
        if payment:
            item['payment'] = payment[0].strip()
        else:
            item['payment'] = unicode('暂无信息', "utf-8")
        guarantee = response.xpath('//div[@class="feiyong_dec"]/ul/li[1]/div[@class="tips-info"]/p[1]/span[3]/b/text()').extract()
        if guarantee:
            item['guarantee'] = guarantee[0].strip()
        else:
            item['guarantee'] = unicode('暂无信息', "utf-8")
        cur_lease = response.xpath('//div[@class="feiyong_dec"]/ul/li[1]/div[@class="tips-info"]/p[2]/span[1]/b/text()').extract()
        if cur_lease:
            item['cur_lease'] = cur_lease[0].strip()
        else:
            item['cur_lease'] = unicode('暂无信息', "utf-8")
        left_lease = response.xpath('//div[@class="feiyong_dec"]/ul/li[1]/div[@class="tips-info"]/p[2]/span[2]/b/text()').extract()
        if left_lease:
            item['left_lease'] = left_lease[0].strip()
        else:
            item['left_lease'] = unicode('暂无信息', "utf-8")
        longest_lease = response.xpath('//div[@class="feiyong_dec"]/ul/li[1]/div[@class="tips-info"]/p[2]/span[3]/b/text()').extract()
        if longest_lease:
            item['longest_lease'] = longest_lease[0].strip()
        else:
            item['longest_lease'] = unicode('暂无信息', "utf-8")
        type_lease = response.xpath('//div[@class="feiyong_dec"]/ul/li/div[@class="tips-info"]/p[3]/span/b/text()').extract()
        if type_lease:
            item['type_lease'] = type_lease[0].strip()
        else:
            item['type_lease'] = unicode('暂无信息', "utf-8")
        yield item