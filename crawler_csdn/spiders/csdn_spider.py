# -*- coding: utf-8 -*-
import scrapy
from crawler_csdn.items import CrawlerCsdnItem


class CsdnSpiderSpider(scrapy.Spider):
    name = 'csdn_spider'
    allowed_domains = ['blog.csdn.net']

    start_urls = ['http://blog.csdn.net/TalonZhang']
    page = 2

    def parse(self, response):

        # 循环博客条目
        blog_list = response.xpath("//main//div[@class='article-list']//div[@class='article-item-box csdn-tracking-statistics']")
        for i_item in blog_list:
            # item 文件导入
            csdn_item = CrawlerCsdnItem()
            # 写详细的 xpath ，进行数据的解析
            csdn_item['blog_number'] = i_item.xpath("./@data-articleid").extract_first()
            csdn_item['blog_title'] = i_item.xpath(".//h4//a/text()[2]").extract()
            csdn_item['blog_address'] = i_item.xpath(".//h4//a/@href").extract_first()

            yield csdn_item

        # 解析下一页规则
        if CsdnSpiderSpider.page < 7:
            next_link = 'http://blog.csdn.net/TalonZhang/article/list/'+str(CsdnSpiderSpider.page)
            CsdnSpiderSpider.page += 1
            yield scrapy.Request(next_link, callback=self.parse)
        pass
