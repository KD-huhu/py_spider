# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import hashlib
import pymongo


class HupunewsPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client['hupu']

    def get_md5(self,value):
        '''
        使用md5的哈希方法对url进行处理，用于判断该ur是否是重复的
        :param value:
        :return:
        '''
        return hashlib.md5(value.encode('utf-8')).hexdigest()


    def process_item(self, item, spider):
        '''
        将获得的字典形式的数据以不重复的方法存入数据库中
        :param item:
        return:
        '''
        # 创建新闻id，这个id是通过新闻url获取的hash值
        item['news_id'] = self.get_md5(item['url'])
        # 使用update更新方法，避免数据的重复
        # 注意在scrapy中item并不是字典结构，在传输时要强制转换为字典格式
        self.db['NBA'].update({'news_id': item['news_id']}, {'$set': dict(item)}, True)
        print(item)
        return item
