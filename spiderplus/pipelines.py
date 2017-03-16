# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class ParserItemPipeline(object):
    def process_item(self, item, spider):

        item['speed'] = float(item['speed'].strip(u'秒'))
        item['connect_time'] = float(item['connect_time'].strip(u'秒'))
        item['port'] = int(item['port'])
        item['trans'] = 1 if item['trans'] == u'高匿' else 0
        if item['alive_time'].find(u'天') != -1:
            item['alive_time'] = int(item['alive_time'].strip(u'天')) * 24 * 60
        elif item['alive_time'].find(u'小时') != -1:
            item['alive_time'] = int(item['alive_time'].strip(u'小时')) * 60
        elif item['alive_time'].find(u'分钟') != -1:
            item['alive_time'] = int(item['alive_time'].strip(u'分钟'))
        return item


class DropItemPipeline(object):
    def process_item(self, item, spider):
        if item['speed'] > 1:
            raise DropItem("Speed is slow (%s)" % item['speed'])
        return item
