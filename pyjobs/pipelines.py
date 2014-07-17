# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from pymongo import MongoClient


class MongoPipeline(object):

    def __init__(self):
        try:
            client = MongoClient()
        except:
            raise Exception("Can't connect to mongodb")

        #use pyjobs database and jobs collection
        self.c = client.pyjobs.jobs

    def process_item(self, item, spider):
        if self.c.find_one({'uid': item['uid']}):
            raise DropItem("%s already recorded" % (item['uid'], ))
        else:
            self.c.insert(item.__dict__.get('_values'))
            print "%s recorded" % (item['uid'],)
            return item
