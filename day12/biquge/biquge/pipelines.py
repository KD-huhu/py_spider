# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import pymongo

class BiqugePipeline:

    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['biquege']


    def get_md5(self,value):
        md5 = hashlib.md5(bytes(value,encoding='utf-8'))
        return md5.hexdigest()


    def process_item(self, item, spider):
        # 按照什么区跟新
        # db.c.update({查询表达式}，{跟新成什么}，{upsert:true})
        item['hash_url'] = self.get_md5(item['chapter_url'])
        self.db['xuanhaun'].update({'hash_url':item['hash_url']},{'$set':dict(item)},{True})
        # print(item)
        return item
