# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from zhaopin.items import ZhaopinItem


class ZhaopininfoSpider(CrawlSpider):
    name = 'zhaopininfo'
    allowed_domains = ['www.51job.com','search.51job.com','jobs.51job.com']
    start_urls = ['http://www.51job.com/']

    rules = (
        # Rule(LinkExtractor(allow="/list/\d+?,\d+?,\d+?", unique=True), follow=True),
        Rule(LinkExtractor(allow="/jobs.51job.com/.*/\d+?.html",unique=True),callback='parse_company',follow=True),
    )
    def parse_mulu(self, response):
        urls = response.xpath(".//div[@class='el']/p[@class='t1 ']//a//@href").getall()
        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse_company, dont_filter=True)
            yield request

    def parse_company(self,response):
        print("<<<<<<<<<爬取中<<<<<<<<<")
        company_name = response.xpath(".//p[@class='cname']/a/text()").get()
        company_status = response.xpath(".//div[@class='cn']/h1/text()").get().replace('/','／')
        money = response.xpath(".//div[@class='cn']/strong/text()").get()
        if not money:
            money = '0'
        msg_type = response.xpath(".//p[@class='msg ltype']/text()").getall()
        msgs=''
        for msg in msg_type:
            msg.replace('\xa0','').strip()
            msgs+=(msg)
        company_welfare = response.xpath(".//div[@class='jtag']//span/text()").getall()
        company_welfares=''
        for c_w in company_welfare:
            company_welfares +=c_w.strip()+' '
        job_infos = response.xpath(".//div[@class='tBorderTop_box']//div[@class='bmsg job_msg inbox']//text()").getall()
        jobinfos=''
        for job_info in job_infos:
            job_info.replace('\r','').replace('\n','').replace(' ','').strip()
            jobinfos += job_info
        jobinfos = jobinfos.replace('。','。\n').replace('；','；\n').replace('：','：\n').replace('微信分享','').replace(';',';\n').strip()
        contact_infos = response.xpath(".//div[@class='tBorderTop_box']//div[@class='bmsg inbox']//p//text()").getall()
        contact_info=''
        for c_i in contact_infos:
            contact_info+= c_i.strip()
        company_infos = response.xpath(".//div[@class='tmsg inbox']/text()").getall()
        company_info=''
        for co_i in company_infos:
            company_info+= (co_i+'\n').strip()
        item = ZhaopinItem(company_name=company_name, company_status=company_status, money=money,msg_type=msgs
                           ,company_welfare=company_welfares,job_infos=jobinfos,contact_infos=contact_info,company_infos=company_info)
        yield item
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

