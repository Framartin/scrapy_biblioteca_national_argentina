# -*- coding: utf-8 -*-
import scrapy


class CatalogoSpider(scrapy.Spider):
    name = 'catalogo'
    allowed_domains = ['catalogo.bn.gov.ar']
    start_urls = ['http://catalogo.bn.gov.ar/']

    def parse(self, response):
        pass
