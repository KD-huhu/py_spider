# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanReadItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    book_url = scrapy.Field()
    author = scrapy.Field()
    abstract = scrapy.Field()
    wordCount = scrapy.Field()
    desc = scrapy.Field()
    read_num = scrapy.Field()
    collect_num = scrapy.Field()
    total_ticket = scrapy.Field()
    monthly_ticket = scrapy.Field()
    book_id = scrapy.Field()

