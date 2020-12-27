# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import os
import csv

class ZhaopinPipeline(object):
    def process_item(self, item, spider):
        path = 'D:/job'
        if not os.path.exists(path):
            os.mkdir(path)

        path =path+ '/' + 'info.csv'
        if not os.path.exists(path):
            os.mkdir(path)

        self.file = open(path, 'a+', encoding='utf-8-sig',newline='')
        csv_writer = csv.writer(self.file)
        csv_writer.writerow([item['company_name'], item['company_status'], item['money'],item['msg_type'],item['company_welfare'],item['job_infos'],item['contact_infos'],item['company_infos']])
        self.file.close()
        print("<<<<<<<<<<<爬取结束<<<<<<<<")
