import hashlib

import pymongo
import redis
import requests
from lxml import etree
from queue import Queue
import threading
'''
1、爬取策略：从一个明星的相关人哪里去找下一个
2、如何爬取的更多
    设置初始任务池--池里面可以放：大陆，港台，韩国，日本，欧美
3、必须要去重--避免死链

'''
class MaoyanActor(threading.Thread):
    def __init__(self,q_actor):
        super().__init__()
        self.q_actor = q_actor
        self.client = pymongo.MongoClient()
        self.db = self.client['maoyan_actor']
        # self.main()


    def get_xpath(self,url):
        '''
        请求url，获取页面内容的element对象
        :param url:
        :return:
        '''
        headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        response = requests.get(url,headers= headers)
        # print(response.status_code)
        return etree.HTML(response.text)

    def get_text(self,text):
        if text:
            return text[0]
        return None


    def get_md5(self,value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()


    def write_to_mongo(self,item):
        #创建新闻id，这个id是通过新闻url获取的hash值
        item['actor_id'] = self.get_md5(item['actor_url'])
        self.db['actor'].update({'actor_id':item['actor_id']},{'$set':item},True)
        # print(item)
    def parse_actor(self,url):
        '''
        解析页面
        :param html: 页面的element对象
        :return: 返回相关人
        '''
        #获取数据
        html = self.get_xpath(url)
        chian_name = self.get_text(html.xpath('//p[@class="china-name cele-name"]/text()'))
        en_name = self.get_text(html.xpath('//p[@class="eng-name cele-name"]/text()'))
        profession = self.get_text(html.xpath('//span[@class="profession"]/text()'))
        birthday = self.get_text(html.xpath('//span[@class="birthday"]/text()'))
        height = self.get_text(html.xpath('//span[@class="height"]/text()'))
        master_works = html.xpath('//ul[@class="master-list"]/li/a/img/@alt')
        desc = self.get_text(html.xpath('//p[@class="cele-desc"]/text()'))
        # print(desc)
        # print(master_works)
        item = {}
        item['chian_name']= chian_name
        item['en_name']= en_name
        item['profession']= profession
        item['birthday']= birthday
        item['height']= height
        item['master_works']= master_works
        item['desc']= desc
        item['actor_url'] = url
        # print(item)
        self.write_to_mongo(item)
        #获取相关人
        relatice_actors = html.xpath('//div[@class="slider rel-slider"]/div[@class="item"]/div/a/@href')
        # print(relatice_actors)
        return relatice_actors

    #主要用redis的set
    def url_seen(self,url):
        '''
        判断url是否重复
        :param url:
        :return:True：重复，False不重复
        '''
        re = redis.Redis()
        result = re.sadd('maoyan_actor_set', url)
        return result == 0

    def main(self):
        while not self.q_actor.empty():
            #两件事：提取信息保存
            #获取相关人，返回
            relative_urls = self.parse_actor(q_actor.get())
            print(self.name)
            # print(relative_urls)
            if relative_urls:
                for url in relative_urls:
                    #/films/celebrity/269699
                    full_url = 'https://maoyan.com'+url
                    #去重判断
                    if not self.url_seen(self.get_md5(full_url)):

                        #没有被爬取过
                        self.q_actor.put(full_url)
    def run(self):
        self.main()

if __name__ == '__main__':

    #start_urls
    actor_urls = [
        'https://maoyan.com/films/celebrity/789',#成龙
        'https://maoyan.com/films/celebrity/3718',
        'https://maoyan.com/films/celebrity/28427',
        'https://maoyan.com/films/celebrity/31444',
        'https://maoyan.com/films/celebrity/8681'
    ]
    #调度器，
    q_actor =Queue()
    for url in actor_urls:
        q_actor.put(url)
    for i in range(4):
        t= MaoyanActor(q_actor)
        t.start()

