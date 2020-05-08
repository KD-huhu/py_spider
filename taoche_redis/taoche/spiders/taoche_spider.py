# -*- coding: utf-8 -*-
import scrapy,re
from scrapy_redis import spiders
from taoche.items import TaocheItem
from taoche.spiders.city import CAR_CODE_LIST,CITY_CODE
import socket

class TaocheSpiderSpider(spiders.RedisSpider):
    name = 'taoche_spider'
    # allowed_domains = ['www']
    # start_urls = []
    # index = 1
    # for city in CITY_CODE:
    #     for car in CAR_CODE_LIST:
    #         base_url = 'https://{}.taoche.com/{}/?page=1'.format(city, car)
    #         start_urls.append(base_url)
    redis_key = 'taoche:start_urls'
    myaddr = socket.gethostbyname(socket.gethostname())

    def parse(self, response):
        #判断一下这个页面中有没有内容
        #如果有内容，解析，解析之后请求下一页，回调自己
        li_list = response.xpath('//div[@id="container_base"]/ul/li')
        if li_list:
            for li in li_list:
                #解析
                car_name = li.xpath('//div[@class="gongge_main"]/a/@title').extract_first()
                infos = li.xpath('.//p/i/text()').extract()
                try:
                    car_year = infos[0]
                    car_lichen = infos[1]
                    car_location = infos[2]
                except Exception:
                    continue
                car_price = li.xpath('.//i[@class="Total brand_col"]/text()').extract_first()
                detail_url = li.xpath('//div[@class="gongge_main"]/a/@href').extract_first()
                item =TaocheItem()
                item['car_name'] = car_name
                item['car_year'] = car_year
                item['car_lichen'] = car_lichen
                item['car_location'] = car_location
                item['car_price'] = car_price
                item['detail_url'] = detail_url
                item['ip'] = self.myaddr
                yield item
            #解析之后请求下一页，回调自己
            url = response.url

            #https://beijing.taoche.com/porsche/?page=2
            p = re.compile(r'page=(\d+)')
            page = int(p.search(url).group(1))+1

            new_url = p.sub('page={}'.format(page),url)
            # print(url,new_url,sep='|-:-|')
            yield scrapy.Request(new_url,callback=self.parse,encoding='utf-8')