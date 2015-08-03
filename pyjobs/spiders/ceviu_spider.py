# -*- coding: utf-8 -*-
import scrapy
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class CeviuSpider(scrapy.Spider):
    name = "ceviu"
    allowed_domains = ["ceviu.com.br", ]
    base_url = "http://ceviu.com.br"
    start_urls = [
        "http://www.ceviu.com.br/buscar/empregos?\
         level=1&novaPesquisa=1&termoPesquisa=python&itensPagina=10000000",
    ]

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "box-vaga")]')
        for i in items:
            job = JobItem()
            link = i.xpath('.//h4/a')

            job['uid'] = i.xpath(
                './/p[@class="info-vaga-detalhe"]/span[2]/text()')\
                .extract()[0].strip()

            job['link'] = "%s%s" % (self.base_url,
                                    link.xpath('@href').extract()[0])
            job['title'] = link.xpath('text()').extract()[0]

            desc = i.xpath(
                './/div[contains(@class, "descricao-vaga")]/p/text()')\
                .extract()[0]
            job['desc'] = clean_str(desc)

            city_state = i.xpath(
                './/p[contains(@class, "info-vaga-conteudo")]/span[2]/text()')\
                .extract()[0].strip()
            job['city'] = city_state.split('/')[0]
            job['state'] = city_state.split('/')[1]

            pay = i.xpath(
                './/p[contains(@class, "info-vaga-conteudo")]/span[1]/text()')\
                .extract()[0].strip()
            job['pay'] = pay

            yield job
