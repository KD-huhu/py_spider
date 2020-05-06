# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    content = scrapy.Field()
    chapter_url = scrapy.Field()
    # 判断重复urlhash值
    hash_url = scrapy.Field()