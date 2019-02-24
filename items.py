# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BjjsItem(scrapy.Item):
    # define the fields for your item here like:
    cert_no = scrapy.Field()
    corp_name = scrapy.Field()
    corp_repr = scrapy.Field()
    admi_code = scrapy.Field()
    regi_addr = scrapy.Field()
    econ_type = scrapy.Field()
    prom_rang = scrapy.Field()
    prom_cell = scrapy.Field()
    chek_date = scrapy.Field()
    last_chek = scrapy.Field()
    post_chek = scrapy.Field()


    pass
