# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BnarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = scrapy.Field()
    doc_number = scrapy.Field()
    item_type = scrapy.Field()
    cdu = scrapy.Field()
    isbn = scrapy.Field()
    title = scrapy.Field()
    printer = scrapy.Field()
    serie = scrapy.Field()
    book_type = scrapy.Field()
    permalink = scrapy.Field()
    notes_list = scrapy.Field()
    file_urls = scrapy.Field()
