# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class EmpregosSpider(CrawlSpider):
    name = "empregos"
    allowed_domains = ["empregos.com.br", ]
    base_url = "http://www.empregos.com.br"
    start_urls = [
        "http://www.empregos.com.br/vagas/python",
    ]

    # rules = (
    #     Rule(LxmlLinkExtractor(),
    #          callback='parse_start_url', follow=True),
    # )

    def parse_start_url(self, response):
        # search quantity pages
        pagination = response.xpath('//div[contains(@class, "paginador")]/ul/li')
        
        # # loop pages and concat with url default
        for page_number in range(1, len(pagination) - 1):
            url_page = response.url + '/p{0}'.format(page_number)
            request = Request(url_page, callback=self.parse_item)
            yield request

    def parse_item(self, response):

        items = response.xpath('//div[contains(@class, "vaga")]')

        count = 0
        for i in items:
            
# 
            #  = i.xpath('link.xpath('@href').extract()[0]')#.extract()[0]# + self.name

            links = i.xpath('//div[contains(@class, "topo")]/h3/a')

            for link in links:
                # print type(link), link
                job = JobItem()

                #print link.xpath('@href').extract()[0]

                job['link'] = link.xpath('@href').extract()[0]

                job['uid'] = job['link'].split('/')[-1] + self.name
                
                job['title'] = link.xpath('text()').extract()[0]

                desc = i.xpath(
                    '//div[contains(@class, "descricao")]/p/text()').extract()[0]

                # print type(desc), len(desc), desc
                job['desc'] = clean_str(desc)

                citystate_string = i.xpath('//div[contains(@class, "topo")]/div[contains(@class, "itensEmpresa")]/span').extract()#[0].split(' ')
                citystate_string = citystate_string[0].split(u'\u2022')[-2].split('/')
                
                #print 'citystate_string', type(citystate_string), citystate_string
                job['city'] = clean_str(citystate_string[0])

                job['state'] = clean_str(citystate_string[1])
                
                job['pay'] = '-'#clean_str(i.xpath('.//p/text()').extract()[0])

                # print job
                yield job
