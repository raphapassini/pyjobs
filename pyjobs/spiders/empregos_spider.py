# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.spiders import Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class EmpregosSpider(CrawlSpider):
    name = "empregos"
    allowed_domains = ["empregos.com.br", ]
    base_url = "http://www.empregos.com.br"
    start_urls = [
        "http://www.empregos.com.br/vagas/python",
    ]

    rules = (
        Rule(LxmlLinkExtractor(
            allow=('python/p[0-9]', )), callback='parse_item'),
    )

    def parse_start_url(self, response):
        yield Request(response.url, callback=self.parse_item)

    def parse_item(self, response):
        items = response.xpath(
            "//ul[@class='list grid-16-16']/li[@class='item']")
        for i in items:
            job = JobItem()
            job['link'] = i.xpath('.//h3/a/@href').extract()[0]
            job['uid'] = '{}_{}'.format(
                job['link'].split('/')[-1], self.name)
            job['title'] = i.xpath('.//h3/a/text()').extract()[0]

            desc = i.xpath(
                '//div[contains(@class, "descricao")]/p/text()'
            ).extract()[0]
            job['desc'] = clean_str(desc)

            citystate_string = clean_str(
                i.xpath(
                    './/span[contains(@class, "nome-empresa")]/text()'
                ).extract()[0]
            )
            citystate_string = citystate_string.strip().split('-')

            try:
                job['city'] = citystate_string[1]
            except IndexError:
                job['city'] = ''

            try:
                job['state'] = citystate_string[2]
            except IndexError:
                job['state'] = ''

            job['pay'] = clean_str(
                i.xpath(".//div[@class='salario-de-ate']/text()").extract()[0])
            yield job
