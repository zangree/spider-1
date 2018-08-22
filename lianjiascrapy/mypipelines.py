# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import DropItem
import json
import codecs


class MyPipeline(object):
    def __init__(self):    
        self.file = codecs.open('szershoufang.json', 'w', encoding='utf-8')

    def _setFileName(self, filename):
        newfilename = filename
        self.file = codecs.open(newfilename, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
