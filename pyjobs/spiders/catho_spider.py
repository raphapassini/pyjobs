# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class CathoSpider(CrawlSpider):
    name = "catho"
    allowed_domains = ["www.catho.com.br", ]
    base_url = "http://www..catho.com.br"
    start_urls = [
        "http://www.catho.com.br/buscar/empregos/?"
        "State=resultado&tipoBusca=palavra_chave&perfil_id=1&"
        "q=Programador+Python&pais_id=31&where_search=1&"
        "how_search=2&inputDate=-1&faixa_sal_id=-1&faixa_sal_id_combinar=1",
    ]

    def parse_start_url(self, response):
        # search quantity pages
        pagination = response.xpath('//ul[@id="navPagin"]/li')
        last_page = pagination.xpath('//a/@data-page').extract()[-2]
        # loop pages and concat with url default
        for page_number in range(1, int(last_page) + 1):
            url_page = response.url + '&page={0}'.format(page_number)
            request = Request(url_page, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        items = response.xpath('//div[contains(@class, "boxVaga")]')
        for i in items:
            job = JobItem()

            job['provider'] = self.name

            job['uid'] = "{}_{}".format(
                i.xpath('@id').extract()[0], self.name)

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
            job['pay'] = clean_str(
                i.xpath('.//div[@class="salarioLocal"]/h3/text()')
                .extract()[0])

            yield job
