import codecs

from scrapy import cmdline
import os
import csv
path = 'D:/job'
if not os.path.exists(path):
    os.mkdir(path)
path = path+ '/' + 'info.csv'
if not os.path.exists(path):
    file = open(path, 'a+', encoding='utf-8-sig',newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(["公司", "职位", "月薪","招收情况","公司福利","职位信息","联系方式","公司信息"])
    file.close()
cmdline.execute("start crawl zhaopininfo".split())