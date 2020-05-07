# -*- coding: utf-8 -*-
import json
import re
import scrapy

from douban_read.items import DoubanReadItem


class ReadSpiderSpider(scrapy.Spider):
    name = 'read_spider'
    # allowed_domains = ['ww']
    start_urls = []
    #用start_urls可以发初始请求，但是他是怎么发的。
        #当scrapy启动的时候，默认加载方法永远只有一个：start_request()
        #start_requerst方法其实就是遍历start_urls，取出url，发送请求
    #当我们重写了start_request,那么当前spiders，tart_urls这个列表就只是一个列表
    #对于初始请求，如果想要想二次请求那样，去自定义一个request对象，如何做？

    #通过一个参数可以标识请求（requet）
    '''
    scrapy.Request(
        meta={type_:'1'}
    )
    '''
    def start_requests(self):
        base_url = 'https://read.douban.com/charts'
        #设置一个flag参数：Flase不适用scrapy下载器
        yield scrapy.Request(base_url,callback=self.parse,encoding='utf-8',meta={'flag':False})


    def parse(self, response):
        # print('in parse')
        # 解析分类url
        type_urls = response.xpath('//div[@class="rankings-nav"]/a[position()>1]/@href').extract()
        # print(type_urls)
        for url in type_urls:
            # /charts?type=unfinished_column&index=featured&dcs=charts&dcm=charts-nav
            p = re.compile(r'type=(.*?)&index=(.*?)&dcs')
            type_ = p.search(url).group(1)
            index = p.search(url).group(2)
            ajax_url = 'https://read.douban.com/j/index//charts?type={}&index={}&verbose=1'.format(type_, index)
            yield scrapy.Request(ajax_url,callback=self.parse_ajax,encoding='utf-8',meta={'flag':True})


    def parse_ajax(self,response):
        '''
        获取每个分类的ajax数据
        :param type_:
        :param index:
        :return:
        '''

        json_str = response.text
        json_data = json.loads(json_str)
        if json_data:
            for data in json_data['list']:
                title = data['works']['title']
                book_url = 'https://read.douban.com'+data['works']['url']
                author = data['works']['author'][0]['name']
                abstract = data['works']['abstract']
                wordCount = data['works']['wordCount']
                item = DoubanReadItem()
                item['title'] = title
                item['book_url'] = book_url
                item['author'] = author
                item['abstract'] = abstract
                item['wordCount'] = wordCount
                #item只处理了一半，剩下一半在另外一个方法中。
                yield scrapy.Request(book_url,callback=self.parse_detail,encoding='utf-8',meta={'flag':True,'data':item})

    def handle_number(self,text):
        '''
        处理带逗号的字符串数字
        :param num:2,111
        :return:
        '''
        if text:
            p = re.compile(r'\d+')
            result = p.findall(text)
            return ''.join(result)

    def parse_detail(self,response):
        url = response.url
        item = response.meta['data']
        if 'ebook' in url:
            desc = response.xpath('string(//div[@class="info"])').extract_first()
            word_num = response.xpath('//span[@class="labeled-text"]/text()').extract_first()
            # 阅读数
            read_num = response.xpath('//span[@class="read-count"]/text()').extract_first()
            # 收藏数
            collect_num = ''
            # 月票数
            monthly_ticket = ''
            # 累计推荐数
            total_ticket = ''
            # print(desc,read_num)
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = collect_num
            item['monthly_ticket'] = monthly_ticket
            item['total_ticket'] = total_ticket
        else:
            desc = response.xpath('string(//div[@class="when-expand"]/p/text()|//div[@class="when-fold"]/text())').extract_first()
            word_num = response.xpath('//div[@class="count-group"]/span[1]/div[2]/text()').extract_first()
            # 阅读数
            read_num = response.xpath('//div[@class="count-group"]/span[2]/div[2]/text()').extract_first()
            # 收藏数
            collect_num = response.xpath('//div[@class="count-group"]/span[3]/div[2]/text()').extract_first()
            # 月票数
            monthly_ticket = response.xpath('//div[@class="count-group"]/span[4]/div[2]/text()').extract_first()
            # 累计推荐数
            total_ticket = response.xpath('//div[@class="count-group"]/span[5]/div[2]/text()').extract_first()
            # print(word_num,read_num,collect_num,monthly_ticket,total_ticket)
            # print(desc)
            item['desc'] = desc
            item['read_num'] = self.handle_number(read_num)
            item['collect_num'] = self.handle_number(collect_num)
            item['monthly_ticket'] = self.handle_number(monthly_ticket)
            item['total_ticket'] = self.handle_number(total_ticket)
        yield item