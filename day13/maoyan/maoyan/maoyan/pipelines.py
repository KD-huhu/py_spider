# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import pymongo

class MaoyanPipeline:
    def process_item(self, item, spider):
        def __init__(self):
            self.client = pymongo.MongoClient()
            self.db = self.client['maoyan_actor1']


        def get_md5(self, value):
            return hashlib.md5(value.encode('utf-8')).hexdigest()


        def process_item(self, item, spider):
            # 创建新闻id，这个id是通过新闻url获取的hash值
            item['actor_id'] = self.get_md5(item['actor_url'])
            self.db['actor'].update({'actor_id': item['actor_id']}, {'$set': item}, True)
            print(item)


        return item
