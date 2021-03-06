import hashlib
import threading
import pymongo
import requests
from lxml import etree
from queue import Queue


class HupuNews(threading.Thread):
    def __init__(self,url,q_page):
        super().__init__()
        self.client = pymongo.MongoClient()
        self.db = self.client['hupu_news']
        self.url = url
        self.q_page = q_page
        # self.main()


    def get_xpath(self,url):
        '''
        请求url，获取页面内容的element对象
        :param url:
        :return:获取页面内容的element对象
        '''
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        }
        response = requests.get(url,headers=headers)
        # print(response.text)
        if response.status_code == 200:
            return etree.HTML(response.text)
        else:
            return None


    def parse_page(self,url):
        '''
        解析每一个分页，获取列表页的url
        :param url:
        :return:每一页中列表的url
        '''
        html = self.get_xpath(url)
        new_urls = html.xpath('//div[@class="news-list"]/ul/li//h4/a/@href')
        # print(new_urls)
        return new_urls


    def get_text(self,text):
        '''
        判断获取的数据内容是否为空
        :param text:
        :return:
        '''
        if text:
            return text[0]
        else:
            return None


    def get_md5(self,value):
        '''
        使用md5的哈希方法对url进行处理，用于判断该ur是否是重复的
        :param value:
        :return:
        '''
        return hashlib.md5(value.encode('utf-8')).hexdigest()


    def write_to_mongo(self,item):
        '''
        将获得的字典形式的数据以不重复的方法存入数据库中
        :param item:
        :return:
        '''
        # 创建新闻id，这个id是通过新闻url获取的hash值
        item['news_id'] = self.get_md5(item['url'])
        # 使用update更新方法，避免数据的重复
        self.db['NBA'].update({'news_id': item['news_id']}, {'$set': item}, True)
        # print(item)


    def parse_detail(self,url):
        '''
        解析详情页，并保存数据
        :param url:
        :return:无
        '''
        html = self.get_xpath(url)
        # 获取数据
        # 标题
        title = self.get_text(html.xpath('//h1[@class="headline"]/text()'))
        # 来源
        source = self.get_text(html.xpath('//span[@id="source_baidu"]/a/text()'))
        # 图片
        images = html.xpath('//div[@class="artical-content"]//img/@src')
        # 内容
        content = html.xpath('string(//div[@class="artical-content"])').strip()
        # 发布时间
        publish_time = self.get_text(html.xpath('//*[@id="pubtime_baidu"]/text()'))
        # 创建字典保存数
        item = {}
        item['title'] = title
        item['source'] = source
        item['images'] = images
        item['content'] = content
        item['publish_time'] = publish_time
        item['url'] = url
        # 测试
        # print(item)
        # 将数据保存在数据库中
        self.write_to_mongo(item)


    def main(self):
        # base_url = 'https://voice.hupu.com/nba/%s'
        # for i in range(1,2):
        #     # 第一步：获取每一页的新闻urls
        #     new_url = self.parse_page(base_url%i)
        #     # 第二步进入详情页
        #     for url in new_url:
        #         # 解析保存
        #         self.parse_detail(url)
        while not self.q_page.empty():
            # 第一步：获取每一页的新闻urls
            page_num = self.q_page.get()
            print('=========第{}页==========@{}'.format(page_num, self.name))
            new_urls = self.parse_page(self.url%page_num)
            # 第二步进入详情页
            for url in new_urls:
                self.parse_detail(url)


    def run(self):
        self.main()


if __name__ == '__main__':
    base_url = 'https://voice.hupu.com/nba/%s'
    # 任务队列放什么
    # 最顶层的循环的条件就是任务队列的内容
    queue_page = Queue()
    for i in range(1,5):
        queue_page.put(i)
    # 创建一个list，这个list的长度就是线程的数量
    for i in range(2):
        t = HupuNews(base_url,queue_page)
        t.start()
