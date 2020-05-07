# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class ActorSpiderSpider(scrapy.Spider):
    name = 'actor_spider'
    # allowed_domains = ['www']
    start_urls = [
        'https://maoyan.com/films/celebrity/789',
        'https://maoyan.com/films/celebrity/3718',
        'https://maoyan.com/films/celebrity/28427',
        'https://maoyan.com/films/celebrity/31444',
        'https://maoyan.com/films/celebrity/8681'
    ]

    def parse(self, response):
        chian_name = response.xpath('//p[@class="china-name cele-name"]/text()').extract_first()
        en_name = response.xpath('//p[@class="eng-name cele-name"]/text()').extract_first()
        profession = response.xpath('//span[@class="profession"]/text()').extract_first()
        birthday = response.xpath('//span[@class="birthday"]/text()').extract_first()
        height = response.xpath('//span[@class="height"]/text()').extract_first()
        master_works = response.xpath('//ul[@class="master-list"]/li/a/img/@alt').extract()
        desc = response.xpath('//p[@class="cele-desc"]/text()').extract_first()
        item = MaoyanItem()
        item['chian_name'] = chian_name
        item['en_name'] = en_name
        item['profession'] = profession
        item['birthday'] = birthday
        item['height'] = height
        item['master_works'] = master_works
        item['desc'] = desc
        item['actor_url'] = response.url

        yield item
        relatice_actors = response.xpath('//div[@class="slider rel-slider"]/div[@class="item"]/div/a/@href').extract()
        if relatice_actors:
            for url in relatice_actors:
                # /films/celebrity/269699
                full_url = 'https://maoyan.com' + url
                yield scrapy.Request(full_url,callback=self.parse,encoding='utf-8')

