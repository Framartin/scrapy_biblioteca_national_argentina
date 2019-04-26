# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BnarPipeline(object):
    def process_item(self, item, spider):
        return item

class StripStrPipeline(object):
    """
    Strip all string fields of items
    """
    def process_item(self, item, spider):
        for k, v in item.items():
            if type(v) == str:
                item[k] = v.strip()
        return item
