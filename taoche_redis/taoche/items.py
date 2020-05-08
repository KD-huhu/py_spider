# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaocheItem(scrapy.Item):
    # define the fields for your item here like:
    car_name = scrapy.Field()
    car_year = scrapy.Field()
    car_lichen = scrapy.Field()
    car_location = scrapy.Field()
    car_price = scrapy.Field()
    detail_url = scrapy.Field()
    car_id = scrapy.Field()
    ip = scrapy.Field()

