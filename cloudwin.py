# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 1:13
# @Author  : 方炯丰
# @Function:
# @File    : cloudwin.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2020/11/29 21:20
# @Author  : 方炯丰
# @Function:用于提取pdf中的关键词，同时转换为词云图片
# @File    : 云词.py
# @Software: PyCharm
import os
import pandas as pd
import jieba as jb
from wordcloud import wordcloud

if __name__ == '__main__':
    df = pd.read_csv('D:/job/info.csv')
    content = "".join(i for i in df['职位信息'])
    content = content
    print(content)
    a= jb.lcut(content)#分词
    b = ' '.join(a)#形成词表
    c = wordcloud.WordCloud(font_path='SIMYOU.TTF',width=1000,height=500)
    c.generate(b)
    c.to_file("pywordcloud1.png")
