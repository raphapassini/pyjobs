# -*- coding: utf-8 -*-

#http://stackoverflow.com/questions/17975471/selenium-with-scrapy-for-dynamic-page
from selenium import webdriver

import scrapy
from pyjobs.items import JobItem
from pyjobs.util import clean_str


class VagasSpider(scrapy.Spider):
    name = "vagas"
    allowed_domains = ["www.vagas.com.br", ]
    base_url = "http://www.vagas.com.br"
    start_urls = [
        "http://www.vagas.com.br/vagas-de-python",
    ]

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            try:
                self.driver.find_element_by_id("maisDoMes").click()
            except:
                break

        items = self.driver.find_elements_by_xpath('//div[@id="vagasDoMes"]/article')

        #items = response.xpath('//div[@id="vagasDoMes"]/article')
        for i in items:
            job = JobItem()
            
            link = i.find_element_by_xpath('.//header/h2[@class="cargo"]/a')

            job['uid'] = link.get_attribute("id") + self.name
            #link.find_element_by_xpath('@id').extract()[0]# + self.name

            job['link'] = link.get_attribute("href")

            #job['title'] = link.find_element_by_xpath('text()').extract()[0]        
            job['title'] = link.get_attribute("title")
            desc = i.find_element_by_xpath('.//div[@class="detalhes"]/p')
            # print desc.get_attribute("innerHTML")
            job['desc'] = desc.text
            job['pay'] = '-'
            
            cityState = i.find_element_by_xpath('.//header/h2[@class="cargo"]/span').text
            cityState = cityState.strip().split('/')
            if len(cityState) == 3:
                job['state'] = cityState[1].strip()
                job['city'] = cityState[0].strip()
            else:
                job['state'] = '-'
                job['city'] = '-'
            # print job
            yield job
        self.driver.close()
