# -*- coding: utf-8 -*-
import scrapy
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class CathoSpider(scrapy.Spider):
    name = "catho"
    allowed_domains = ["home.catho.com.br", ]
    base_url = "http://home.catho.com.br"
    start_urls = [
        "http://home.catho.com.br/buscar/empregos/?\
        State=resultado&tipoBusca=palavra_chave&perfil_id=1&\
        q=Programador+Python&pais_id=31&where_search=1&\
        how_search=2&inputDate=-1&faixa_sal_id=-1&faixa_sal_id_combinar=1",
    ]

    def __init__(self, *args, **kwargs):
        super(CathoSpider, self).__init__(*args, **kwargs)
        self.page = 2

    def parse(self, response):
        print response.body
        print '-------------------------------------------------<'
        items = response.xpath('//div[contains(@class, "boxVaga")]')
        for i in items:
            job = JobItem()

            job['uid'] = i.xpath('@id').extract()[0]

            link = i.xpath('.//h2[@itemprop="title"]/a')
            job['link'] = link.xpath('@href').extract()[0]
            job['title'] = link.xpath('text()').extract()[0]

            desc = i.xpath(
                './/div[contains(@itemprop, "description")]/text()'
            ).extract()[0]
            job['desc'] = clean_str(desc)
            job['city'] = clean_str(i.xpath(
                './/span[contains(@itemprop, "addressRegion")]/text()'
            ).extract()[0])
            job['state'] = clean_str(i.xpath(
                './/span[contains(@itemprop, "addressLocality")]/text()'
            ).extract()[0])
            job['pay'] = clean_str(i.xpath('.//p/text()').extract()[0])

            yield job

        #go next page
        data = {
            'perfil_id': '1',
            'q': 'Programador Python',
            'pais_id': '31',
            'where_search': '1',
            'how_search': '2',
            'faixa_sal_id_combinar': '1',
            'page': '2',
            'cargoslug': 'programador-python',
            'cargotitulo': 'Programador Python',
        }
        yield scrapy.FormRequest(
            "http://home.catho.com.br/buscar/empregos/ajax/",
            formdata=data, callback=self.parse)
