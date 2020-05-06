# -*- coding: utf-8 -*-
import scrapy

from maoyan.items import MaoyanItem


class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_spider'
    # allowed_domains = ['www']
    start_urls = []
    # 分页做法
    for i in range(10):
        base_url = 'https://maoyan.com/board/4?offset=%s' % (i*10)
        start_urls.append(base_url)


    def parse(self, response):
        # 测试下载器下载好的response有没有数据
        # print(response.text)
        # 提取数据
        # 实例化定义好的item，注意要将该包导入
        item = MaoyanItem()
        '''
        response对象的xpath方法:不需要使用lxml在转
        responsex.xpath('xpath表达式')--返回值：[selector对象]
        从selector中提取数据的方法:
            responsex.xpath('xpath表达式').extract_first()-就是一个字符串
            responsex.xpath('xpath表达式').extract()---返回值是list，list里面是所有的字符串内容
        '''
        dd_list = response.xpath('//div[@class="main"]/dl/dd')
        for dd in dd_list:
            movie_title = dd.xpath('.//p[@class="name"]/a/@title').extract_first()
            # print(movie_title)
            movie_actor = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            date = dd.xpath('.//p[@class="releasetime"]/text()').extract_first()
            scores = dd.xpath('.//p[@class="score"]/i/text()').extract()
            detail = dd.xpath('.//p[@class="name"]/a/@href').extract_first()
            # print(scores)
            scores = ''.join(scores)
            item['movie_title'] = movie_title
            item['movie_actor'] = movie_actor
            item['date'] = date
            item['detail'] = detail
            item['scores'] = scores
            # print(item)
            yield item