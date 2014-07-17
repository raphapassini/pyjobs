# -*- coding: utf-8 -*-

# Scrapy settings for pyjobs project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pyjobs'

SPIDER_MODULES = ['pyjobs.spiders']
NEWSPIDER_MODULE = 'pyjobs.spiders'

ITEM_PIPELINES = {
    'pyjobs.pipelines.MongoPipeline': 0,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pyjobs (+http://www.yourdomain.com)'
