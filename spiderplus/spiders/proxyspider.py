# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from scrapy.selector import Selector
from spiderplus.items import proxyItem

class ProxySpider(scrapy.Spider):
    name = "proxyspider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
    ]
    URL = 'http://www.xicidaili.com/nn/%s'
    for i in range(1, 1):
        start_urls.append(URL % str(i))

    def parse(self, response):
        sel = Selector(response)  # Xpath选择器
        for ip in sel.xpath('//tr[@class="odd"]'):
            # print ip.extract()
            result = proxyItem()
            li = ip.xpath('./td')
            result['country'] = (li[0].xpath('./td/img/@alt').extract() + [''])[0]
            result['ip'] = (li[1].xpath('./text()').extract() + [''])[0]
            result['port'] = (li[2].xpath('./text()').extract() + [''])[0]
            result['addr'] = (li[3].xpath('./td/a/text()').extract() + [''])[0]
            result['trans'] = (li[4].xpath('./text()').extract() + [''])[0]
            result['method'] = (li[5].xpath('./text()').extract() + [''])[0]
            result['speed'] = li[6].xpath('./div/@title').extract()[0].strip(u'秒')
            result['connect_time'] = li[7].xpath('./div/@title').extract()[0].strip(u'秒')
            result['alive_time'] = (li[8].xpath('./text()').extract() + [''])[0]
            result['verify_time'] = (li[9].xpath('./text()').extract() + [''])[0]
            yield result
