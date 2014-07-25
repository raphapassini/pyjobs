# -*- coding: utf-8 -*-
# Config Django web project
# import os
# import sys

# BASE_DIR = os.path.dirname(__file__)
# WEB_DIR = os.path.join(BASE_DIR, 'web')

# sys.path.append(WEB_DIR)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'web.settings'


# Config Scrapy
BOT_NAME = 'pyjobs'
SPIDER_MODULES = ['pyjobs.spiders']
NEWSPIDER_MODULE = 'pyjobs.spiders'
ITEM_PIPELINES = {
    'scrapy_mongodb.MongoDBPipeline': 0,
}


# Config MongoDB
MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'pyjobs'
MONGODB_COLLECTION = 'jobs'
MONGODB_UNIQUE_KEY = 'uid'
