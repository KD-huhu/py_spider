import hashlib

import pymongo

class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
        爬虫启动之后，这个方法被执行
        :param crawler:
        :return:
        '''
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        '''
        性能意义所在：
        :param spider:
        :return:
        '''
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def get_md5(self, value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()

    def process_item(self, item, spider):
        # 创建新闻id，这个id是通过新闻url获取的hash值
        item['car_id'] = self.get_md5(item['detail_url'])
        self.db['car'].update({'car_id': item['car_id']}, {'$set': dict(item)}, True)
        print(item)
        return item



