# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    houseInfo = scrapy.Field()
    positionInfo = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice = scrapy.Field()
    region = scrapy.Field()
    taxfree = scrapy.Field()
    haskey = scrapy.Field()
    subway =scrapy.Field()
    
     
class LJbjxiaoquItem(scrapy.Item):
    bjxiaoqu_url = scrapy.Field()
    bjxiaoqu_name = scrapy.Field()
    bjxiaoqu_price = scrapy.Field()


class SFbjxiaoquItem(scrapy.Item):
    sfbjxq_url = scrapy.Field()
    sfbjxq_name = scrapy.Field()
    sfbjxq_price = scrapy.Field()


class LJcjItem(scrapy.Item):
    title = scrapy.Field()
    dealDate = scrapy.Field()
    totalPrice = scrapy.Field()
    unitPrice =  scrapy.Field()
    houseInfo = scrapy.Field()
    positionInfo = scrapy.Field()


class XiezilouItem(scrapy.Item):
    title = scrapy.Field()    
    url = scrapy.Field()


class XiezilouDetailItem(scrapy.Item):
    loupanmingcheng = scrapy.Field()
    jianjie = scrapy.Field() 
    suoshuquyu = scrapy.Field() # 朝阳望京街与阜安西路交叉路口（望京街中部）
    loupandizhi = scrapy.Field()
    huanxianweizhi = scrapy.Field() 
    wuyeleixing = scrapy.Field() 
    xieziloudengji =  scrapy.Field()
    jianzhuleibie =scrapy.Field()
    zongcengshu = scrapy.Field()
    kaifashang = scrapy.Field()
    wuyegongsi = scrapy.Field()
    jungongshijian = scrapy.Field()
    defanglv = scrapy.Field()
    wuyefei = scrapy.Field()
    zhandimianji = scrapy.Field()
    jianzhumianji = scrapy.Field()
    kaijianmianji = scrapy.Field()
    shifoukefenge = scrapy.Field()
    shifoushewai = scrapy.Field()
    diantishuliang = scrapy.Field()
    kongtiaoleixing = scrapy.Field()
    zhuangxiuzhuangkuang = scrapy.Field()
    tingchewei = scrapy.Field()
    louneipeitao = scrapy.Field()


class FangShangPuURL(scrapy.Item):
    shangpu = scrapy.Field()
    url = scrapy.Field()

    
class FangShangPuDetItem(scrapy.Item):    
    shangpu = scrapy.Field()
    quyu = scrapy.Field()
    dizhi = scrapy.Field()
    huanxianweizhi = scrapy.Field()
    jianzhuleibie = scrapy.Field()
    kaifashang = scrapy.Field()
    wuyefei = scrapy.Field()
    zhandimianji = scrapy.Field()
    diantishuliang = scrapy.Field()
    zhuangxiuzhuangkuang = scrapy.Field()
    loupandizhi = scrapy.Field()
    wuyeleibie = scrapy.Field()
    zongcengshu = scrapy.Field()
    jungongshijian = scrapy.Field()
    wuyegongsi = scrapy.Field()
    jianzhumianji = scrapy.Field()
    shifoukefenge = scrapy.Field()
    tingchewei = scrapy.Field()


class FangXiaoQuDanJiaItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class LJXiaoquDanjiaItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()


class YoupuItem(scrapy.Item):
    title = scrapy.Field()


class LePuShangPuURLItem(scrapy.Item):
    shangpu = scrapy.Field()
    url = scrapy.Field()


class LePuShangPuDetItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    update = scrapy.Field()
    area =scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    transfer = scrapy.Field()
    tag1 = scrapy.Field()
    tag2 = scrapy.Field()
    tag3 = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
    running = scrapy.Field()
    license = scrapy.Field()
    shoptype = scrapy.Field()
    floor = scrapy.Field()
    width = scrapy.Field()
    depth = scrapy.Field()
    height =scrapy.Field()
    ring = scrapy.Field()
    street = scrapy.Field()
    neighborhood = scrapy.Field()
    payment = scrapy.Field()
    guarantee = scrapy.Field()
    cur_lease = scrapy.Field()
    left_lease = scrapy.Field()
    longest_lease = scrapy.Field()
    type_lease = scrapy.Field()
    description = scrapy.Field()
    price_around = scrapy.Field()
    lng = scrapy.Field() # 经度
    lat = scrapy.Field() # 纬度
    website = scrapy.Field()

class LianJiaXiaoQuItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
