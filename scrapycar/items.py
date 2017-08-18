# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst


class CarItem(scrapy.Item):
    #车品牌
    carbrand=scrapy.Field()
    #车logo
    logo=scrapy.Field()
    #车的首拼音
    pinyin=scrapy.Field()

    cartype=scrapy.Field()

    carmodel=scrapy.Field()

class SeriesItem(scrapy.Item):
    series_id = scrapy.Field(
        input_processor=MapCompose(lambda v: v.strip("/")),
        output_processor=TakeFirst()
    )
    series_name = scrapy.Field(output_processor=TakeFirst())
