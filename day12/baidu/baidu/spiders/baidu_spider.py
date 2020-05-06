# -*- coding: utf-8 -*-
import scrapy


class BaiduSpiderSpider(scrapy.Spider):
    # spider的名称---将来启动spider爬虫的需要使用
    name = 'baidu_spider'
    # 二次请求需求下载的域名
    # allowed_domains = ['www']
    # 需要让scrapy开始爬取的url，相当于我们之前项目的base_url
    # 只需要将base_Url 放入这个start_urls中，scrapy启动之后，就会从里面取url进行下载。
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        '''
        处理下载器传送过来的response
        处理response，提取数据，或者发送二次请求。
        :param response:
        :return:
        '''
        # response:
        # 获取响应的内容
        # response.text---str类型
        # response.body ---bytes类型
        print('下载成功！')
        with open('baidu.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
        print('写入成功！')
