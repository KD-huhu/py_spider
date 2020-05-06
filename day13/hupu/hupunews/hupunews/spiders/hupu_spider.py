# -*- coding: utf-8 -*-
import scrapy

from hupunews.items import HupunewsItem


class HupuSpiderSpider(scrapy.Spider):
    name = 'hupu_spider'
    # allowed_domains = ['www']
    start_urls = []
    base_url = 'https://voice.hupu.com/nba/%s'
    for i in range(1,5):
        start_urls.append(base_url%i)


    def parse(self, response):
        new_urls = response.xpath('//div[@class="news-list"]/ul/li//h4/a/@href').extract()
        # print(new_urls)
        for url in new_urls:
            # 二次申请
            yield scrapy.Request(url,callback=self.parse_detail,encoding='utf-8')


    def parse_detail(self,response):
        '''
               解析详情页，并保存数据
               :param url:
               :return:无
               '''
        # html = self.get_xpath(url)
        # 获取数据
        # 标题
        title = response.xpath('//h1[@class="headline"]/text()').extract_first()
        # 来源
        source = response.xpath('//span[@id="source_baidu"]/a/text()').extract_first()
        # 图片
        images = response.xpath('//div[@class="artical-content"]//img/@src').extract()
        # 内容
        content = response.xpath('string(//div[@class="artical-content"])').extract_first().strip()
        # 发布时间
        publish_time = response.xpath('//*[@id="pubtime_baidu"]/text()').extract_first()
        # 创建字典保存数
        item = HupunewsItem()

        item['title'] = title
        item['source'] = source
        item['images'] = images
        item['content'] = content
        item['publish_time'] = publish_time
        item['url'] = response.url
        # 测试
        # print(item)
        # 将数据保存在数据库中
        yield item