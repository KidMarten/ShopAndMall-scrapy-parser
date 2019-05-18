# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopandmallscItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    name = scrapy.Field()
    gla = scrapy.Field()
    city = scrapy.Field()
    url = scrapy.Field()
