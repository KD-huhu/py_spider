import hashlib
import pymongo
import requests
from lxml import etree
from city import CITY_CODE,CAR_CODE_LIST

class Taoche(object):
    def __init__(self,url):
        self.url = url
        self.proxies = self.get_proxies()
        self.client = pymongo.MongoClient()
        self.db = self.client['taoche']
        self.parse()


    def get_proxies(self):
        '''
        既可以用于有代理池的情况，又可以用于没有代理池的情况
        :return:None:代理池请求异常，返回None
        '''
        proxy = ''
        try:
            # 启动了代理池
            response = requests.get('http://localhost:5000/get')
            proxy = response.text
            proxies = {
                'http': 'http://' + proxy
            }
            return proxies
        except Exception:
            return None


    def get_md5(self, value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()


    def write_to_mongo(self, item):
        # 创建新闻id，这个id是通过新闻url获取的hash值
        item['car_id'] = self.get_md5(item['detail_url'])
        self.db['car'].update({'car_id': item['car_id']}, {'$set': item}, True)
        print(item)


    def get_xpath_by_requests(self, url):
        # 在这个方法获取一个代理太浪费了。
        # 对于一个代理来说，用它请求出问题，我们才需要跟换。
        # print(self.proxies)
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        try:
            response = requests.get(url, headers=headers, proxies=self.proxies)
            return etree.HTML(response.text)
        except Exception:
            print('代理异常！', self.proxies.get('http', default='代理池未启动！'))
            # 在重新给代理赋值
            self.proxies = self.get_proxies()
            # 重新调用方法继续请求
            return self.get_xpath_by_requests(url)


    def get_text(self, text):
        if text:
            return text[0]
        return ''


    def parse_li(self,li_list):
        for li in li_list:
            item = {}
            try:
                car_name = self.get_text(li.xpath('//div[@class="gongge_main"]/a/@title'))
                infos = li.xpath('.//p/i/text()')
                car_year = infos[0]
                car_lichen = infos[1]
                car_location = infos[2]
                car_price = self.get_text(li.xpath('.//i[@class="Total brand_col"]/text()'))
                detail_url = self.get_text(li.xpath('//div[@class="gongge_main"]/a/@href'))
                item['car_name'] = car_name
                item['car_year'] = car_year
                item['car_lichen'] = car_lichen
                item['car_location'] = car_location
                item['car_price'] = car_price
                item['detail_url'] = detail_url
                # print(item)
                self.write_to_mongo(item)
            except Exception:
                continue


    def parse(self):
        index = 1
        # 分页
        while True:
            html = self.get_xpath_by_requests(self.url + '?page={}'.format(index))
            li_list = html.xpath('//div[@id="container_base"]/ul/li')
            if not li_list:
                break
            self.parse_li(li_list)
            index += 1


if __name__ == '__main__':
    start_urls = []
    # 生成带爬取的url列表
    for city in CITY_CODE:
        for car in CAR_CODE_LIST:
            base_url = 'https://{}.taoche.com/{}/'.format(city, car)
            start_urls.append(base_url)
    for url in start_urls:
        Taoche(url)