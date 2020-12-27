# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    company_name = scrapy.Field()#公司
    company_status= scrapy.Field()#职位
    money = scrapy.Field()#月薪
    msg_type = scrapy.Field()#招收情况
    company_welfare = scrapy.Field()#公司福利
    job_infos = scrapy.Field()#职位信息
    contact_infos = scrapy.Field()#联系方式
    company_infos = scrapy.Field()#公司信息

