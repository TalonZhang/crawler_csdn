# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerCsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 序号
    blog_number = scrapy.Field()
    # 标题
    blog_title = scrapy.Field()
    # 网址
    blog_address = scrapy.Field()

    # 内容
    blog_content = scrapy.Field()

    pass
