# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

class OilItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field(
            input_processor = MapCompose(remove_tags,remove_whitespace),
            output_processor = TakeFirst()
            )
    
    Open_price = scrapy.Field(
            input_processor = MapCompose(remove_tags,remove_whitespace),
            output_processor = TakeFirst()
            )
    
    High_price = scrapy.Field(
            input_processor = MapCompose(remove_tags,remove_whitespace),
            output_processor = TakeFirst()
            )
    
    Low_price = scrapy.Field(
            input_processor = MapCompose(remove_tags,remove_whitespace),
            output_processor = TakeFirst()
            )
    
    Close_price = scrapy.Field(
            input_processor = MapCompose(remove_tags,remove_whitespace),
            output_processor = TakeFirst()
            )

    Adj_Close = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )

    Volume = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )