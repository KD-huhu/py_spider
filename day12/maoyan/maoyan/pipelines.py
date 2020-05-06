# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class MaoyanPipeline:

    def __init__(self):
        # mongo连接
        self.client = pymongo.MongoClient()
        # 连接的数据库
        self.db = self.client['maoyan']


    def process_item(self, item, spider):
        # 将数据插入到数据库
        # insert方法插入时候需要传入dict
        # item本身是一个类，所以需要强转
        self.db['movie'].insert(dict(item))
        # 之所以return，其实就是将item交给其他管道取处理
        # 如果只有一个，这item就处理完成了，在spider中就可以yield下一个了。
        return item
