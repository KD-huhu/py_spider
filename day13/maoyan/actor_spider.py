# -*- coding: utf-8 -*-
import scrapy


class ActorSpiderSpider(scrapy.Spider):
    name = 'actor_spider'
    allowed_domains = ['www']
    start_urls = ['http://www/']

    def parse(self, response):
        pass
