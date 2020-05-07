# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    chian_name = scrapy.Field()
    en_name = scrapy.Field()
    profession = scrapy.Field()
    birthday = scrapy.Field()
    height = scrapy.Field()
    master_works = scrapy.Field()
    actor_url = scrapy.Field()
    desc = scrapy.Field()
    actor_id = scrapy.Field()
