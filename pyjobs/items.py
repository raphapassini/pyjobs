# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class JobItem(scrapy.Item):
    provider = scrapy.Field()
    uid = scrapy.Field()
    link = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    pay = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    # created = scrapy.Field()
    # modefied = scrapy.Field()
