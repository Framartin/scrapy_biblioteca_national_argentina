# -*- coding: utf-8 -*-
import scrapy


class CatalogoSpider(scrapy.Spider):
    name = 'catalogo'
    allowed_domains = ['catalogo.bn.gov.ar']
    supported_fields = [
        'Portada',
        'No. de sistema',
        'Formato',
        'CDU',
        'ISBN',
        'Título',
        'Pie de imprenta',
        'Descrip. física',
        'Género/Forma',
        'Serie',
        'Nota',
        'Doc. digitales',
        'Link al registro',
        # not extracted, b/c not valuable
        'Solicitar en',
    ]

    def __init__(self, *args, **kwargs):
        urls = kwargs.pop('urls', [])
        if urls:
            self.start_urls = urls.split(',')
        self.logger.info(self.start_urls)
        super(CatalogoSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        for href in response.xpath('//div[@id="results"]//a/@href'):
            yield response.follow(href, callback=self.parse_item)

    def parse_item(self, response):
        table = response.xpath('//table[@id="full-table"]')
        url_img = table.xpath("./tr/td[contains(., 'Portada')]//following-sibling::td//img/@src").get()
        doc_number = table.xpath("./tr/td[contains(., 'No. de sistema')]//following-sibling::td/text()").get()
        #permalink = 'https://catalogo.bn.gov.ar/F/?func=direct&doc_number={doc_number}&local_base=GENER'.format(doc_number=doc_number)
        # Example : https://catalogo.bn.gov.ar/F/?func=direct&doc_number=001442521&local_base=GENER
        item_type = table.xpath("./tr/td[contains(., 'Formato')]//following-sibling::td/text()").get()
        cdu = table.xpath("./tr/td[contains(., 'CDU')]//following-sibling::td/text()").get()
        isbn = table.xpath("./tr/td[contains(., 'ISBN')]//following-sibling::td/text()").get()
        title = table.xpath("./tr/td[contains(., 'Título')]//following-sibling::td/text()").get()
        printer = table.xpath("./tr/td[contains(., 'Pie de imprenta')]//following-sibling::td/text()").get()
        serie = table.xpath("./tr/td[contains(., 'Serie')]//following-sibling::td/text()").get()
        book_type = table.xpath("./tr/td[contains(., 'Género/Forma')]//following-sibling::td/text()").get()
        permalink = table.xpath("./tr/td[contains(., 'Link al registro')]//following-sibling::td/a/@href").get()
        notes_list = table.xpath("./tr/td[contains(., 'Nota')]//following-sibling::td/text()").getall()
        # generally a pdf
        url_file = table.xpath("./tr/td[contains(., 'Doc. digitales')]//following-sibling::td/a/@href").re_first('open_window\("(.*?)"\)')
        # log unsupported fields to improve metadata coverage
        # TODO
        fields = table.xpath("./tr/td[1]/text()").getall()
        fields = [x.strip() for x in fields]
        unsupported_fields = [x for x in fields if x not in CatalogoSpider.supported_fields and x != '']
        if unsupported_fields:
            # unique values
            unsupported_fields = list(set(unsupported_fields))
            self.logger.info('The following fields are not supported in {0}: {1}'.format(response.url, unsupported_fields))
        import pdb; pdb.set_trace()
