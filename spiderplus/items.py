# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderplusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class proxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()
    addr = scrapy.Field()
    trans = scrapy.Field()
    method = scrapy.Field()
    speed = scrapy.Field()
    connect_time = scrapy.Field()
    alive_time = scrapy.Field()
    verify_time = scrapy.Field()
   
    

