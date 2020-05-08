# -*- coding: utf-8 -*-
import scrapy

from ..items import BiqugeItem


class BqgSpiderSpider(scrapy.Spider):
    name = 'bqg_spider'
    # allowed_domains = ['wwww']
    start_urls = ['http://www.xbiquge.la/xuanhuanxiaoshuo/']

    def parse(self, response):
        # print(response.text)
        # 获取所有书的url
        book_list = response.xpath('//div[@class="l"]/ul/li/span[1]/a/@href').extract()
        # print(book_list)
        for url in book_list:
            # print(url)
            # 发送二次请求
            yield scrapy.Request(url,callback=self.parse_book,encoding='utf-8')

    # 在每本书的页面中获取章节url
    def parse_book(self,response):
        # print(response.url)
        chapter_urls = response.xpath('//div[@id="list"]/dl/dd/a/@href').extract()
        # print(chapter_urls)
        for url in chapter_urls:
            # 将相对url变成绝对url
            full_url = response.urljoin(url)
            print(full_url)
            yield scrapy.Request(full_url,callback=self.parse_chapter,encoding='utf-8')

    # 解析章节，提取数据
    def parse_chapter(self,response):
        # 提取数据
        item = BiqugeItem()
        book_name = response.xpath('//div[@class="con_top"]/a[3]/text()').extract_first()
        # print(book_name)
        chapter_name = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        content = response.xpath('string(//div[@id="content"])').extract_first()
        chapter_url = response.url
        item['book_name'] = book_name
        item['chapter_name'] = chapter_name
        item['content'] = content
        item['chapter_url'] = chapter_url
        # print(item)
        yield item