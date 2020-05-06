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
    movie_title = scrapy.Field()
    movie_actor = scrapy.Field()
    date = scrapy.Field()
    scores = scrapy.Field()
    detail = scrapy.Field()