# -*- coding: utf-8 -*-
import scrapy


class TencentSpiderSpider(scrapy.Spider):
    name = 'tencent_spider'
    # allowed_domains = ['www']
    start_urls = []
    for i in range(1,2):
        base_url = 'https://careers.tencent.com/search.html?index=%s' % i
        start_urls.append(base_url)

    def parse(self, response):
        # print(response.text)
        print('in parse')
        # 提取数据
        # pass
