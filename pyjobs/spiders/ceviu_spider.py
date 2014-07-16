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
         level=1&novaPesquisa=1&termoPesquisa=python",
    ]

    def parse(self, response):
        items = response.xpath('//div[contains(@class, "boxVaga")]')
        for i in items:
            job = JobItem()
            link = i.xpath('.//span[@class="tituloVaga"]/a')

            job['link'] = "%s%s" % (self.base_url,
                                    link.xpath('@href').extract()[0])
            job['title'] = link.xpath('text()').extract()

            desc = i.xpath(
                './/div[contains(@id, "descricao")]/text()').extract()[0]
            job['desc'] = clean_str(desc)

            cityState = clean_str(i.xpath(
                './/div[contains(@id, "cidadeEstado")]/text()').extract()[0])
            job['state'] = cityState.split('/')[1]
            job['city'] = cityState.split('/')[0]

            pay = clean_str(i.xpath(
                './/div[contains(@id, "salario")]').xpath(
                'text()').extract()[1])
            job['pay'] = pay

            yield job
