# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# from settings import PROXIES
import random
import base64


class LianjiascrapySpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        PROXIES = [
            {'ip_port': '27.184.131.204:8888', 'user_pass': ''},
            # {'ip_port': '1.28.246.144:8080', 'user_pass': ''}, 
            # {'ip_port': '61.176.215.34:8080', 'user_pass': ''},
            # {'ip_port': '117.135.251.209:80', 'user_pass': ''},
            # {'ip_port': '171.38.94.21:8123', 'user_pass': ''},
            # {'ip_port': '58.221.38.70:8080', 'user_pass': ''}, # 403
            # {'ip_port': '', 'user_pass': ''},
            # {'ip_port': '', 'user_pass': ''},
        ]
        proxy = random.choice(PROXIES)
        if proxy['user_pass'] is not None:
            request.meta['proxy'] = 'http://%s' % proxy['ip_port']
            encoded_user_pass = base64.encodestring(proxy['user_pass'])
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
            print "***ProxyMiddleware have pass***" + proxy['ip_port']
        else:
            print "***ProxyMiddleware no pass***" + proxy['ip_port']
            request.meta['proxy'] = proxy['ip_port']