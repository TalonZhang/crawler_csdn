# -*- coding: utf-8 -*-
import scrapy
from crawler_csdn.items import CrawlerCsdnItem
from crawler_csdn.spiders.geturl import CrawlerCsdnGetUrl


class ArticleSpiderSpider(scrapy.Spider):

    index = 0
    url_list = CrawlerCsdnGetUrl().get_url_list()
    name = 'article_spider'
    allowed_domains = ['blog.csdn.net']
    start_urls = [url_list[index]]


    def parse(self, response):

        csdn_item = CrawlerCsdnItem()
        csdn_item['blog_title'] = \
            response.xpath(
                "//main//div[@class='blog-content-box']//div//div//div[1]//h1/text()"
            ).extract_first()
        csdn_item['blog_content'] = \
            response.xpath("//article").extract_first()
        yield csdn_item

        if self.index < len(self.url_list)-1:
            self.index += 1
            next_link = self.url_list[self.index]
            yield scrapy.Request(next_link, callback=self.parse)
        pass
