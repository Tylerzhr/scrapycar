# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarBrandItem(scrapy.Item):
    #车品牌
    carbrand=scrapy.Field()
    #车logo
    logo=scrapy.Field()
    #车的首拼音
    pinyin=scrapy.Field()

    cartype=scrapy.Field()