import hashlib
import pymongo
import redis
import requests
from lxml import etree
from queue import Queue


def get_xpath(url):
    '''
    请求url，获取页面内容的element对象
    :param url:
    :return:
    '''
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    return etree.HTML(response.text)


def get_text(text):
    # 判断获得的数据是否为空
    if text:
        return text[0]
    return None


def get_md5(value):
    # 是用md5加密算法对full_url加密成为哈希结构，查询速度快
    return hashlib.md5(value.encode('utf-8')).hexdigest()


def write_to_mongo(item):
    # 创建新闻id，这个id是通过新闻url获取的hash值
    item['actor_id'] = get_md5(item['actor_url'])
    db['actor'].update({'actor_id': item['actor_id']}, {'$set': item}, True)


def parse_actor(url):
    '''
    解析页面
    :param url:页面的url
    :return:返回相关人列表
    '''
    html = get_xpath(url)
    chian_name = get_text(html.xpath('//p[@class="china-name cele-name"]/text()'))
    en_name = get_text(html.xpath('//p[@class="eng-name cele-name"]/text()'))
    profession = get_text(html.xpath('//span[@class="profession"]/text()'))
    birthday = get_text(html.xpath('//span[@class="birthday"]/text()'))
    height = get_text(html.xpath('//span[@class="height"]/text()'))
    master_works = html.xpath('//ul[@class="master-list"]/li/a/img/@alt')
    desc = get_text(html.xpath('//p[@class="cele-desc"]/text()'))
    item = {}
    item['chian_name'] = chian_name
    item['en_name'] = en_name
    item['profession'] = profession
    item['birthday'] = birthday
    item['height'] = height
    item['master_works'] = master_works
    item['desc'] = desc
    item['actor_url'] = url
    write_to_mongo(item)
    print(item)
    relatice_actors = html.xpath('//div[@class="slider rel-slider"]/div[@class="item"]/div/a/@href')
    # print((relatice_actors))
    return relatice_actors


def url_seen(url):
    '''
    去重操作，主要使用redis的set方法
    :param param:
    :return: True：重复，False不重复
    '''
    re = redis.Redis()
    result = re.sadd('maoyan_actor_set',url)
    return result==0


def main():
    # 两件事：提取信息保存
    while not q_actor.empty():
        # 获取相关人，返回
        reletive_urls = parse_actor(q_actor.get())
        if reletive_urls:
            for url in reletive_urls:
                full_url = 'https://maoyan.com' + url
                # 去重判断
                if not url_seen(get_md5(full_url)):
                    # 没有被爬取过
                    q_actor.put(full_url)
                    # print(q_actor)


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client['maoyan_actor']
    # base_start_urls
    actors_urls = ['https://maoyan.com/films/celebrity/789',
                   'https://maoyan.com/films/celebrity/3718',
                   'https://maoyan.com/films/celebrity/28427',
                   'https://maoyan.com/films/celebrity/31444',
                   'https://maoyan.com/films/celebrity/8681']
    # 调度器
    q_actor = Queue()
    for url in actors_urls:
        q_actor.put(url)
    main()