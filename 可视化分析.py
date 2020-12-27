# -*- coding: utf-8 -*-
# @Time    : 2020/12/27 0:16
# @Author  : 方炯丰
# @Function:
# @File    : 可视化分析.py
# @Software: PyCharm
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from pandocfilters import Math


def jisuan(x):
    if x=='0' or '':
        return 0
    k= x.split('-')
    x1 = float(k[0])
    x2 = k[1].split('/')[0][-1]
    x3 = k[1].split('/')[1]
    if x2 =='千':
        res = x1*1000
        if x3 =='年':
            res = res/12
    elif x2 =='万':
        res = x1*10000
        if x3 =='年':
            res = res/12
    else:
        res =0
    return res
df = pd.read_csv("D:/job/info.csv")
yx =df['月薪']
yx = yx.apply(lambda row:jisuan(row))
sections = [0, 6000,8000, 10000, 15000,20000,999999999999]
group_names = ['0-6000', '6000-8000', '8000-10000', '10000-15000', "Over 20000", '15000-20000']
cuts = pd.cut(numpy.array(yx), sections, labels=group_names)
counts = pd.value_counts(cuts)
print(counts)
counts.plot.bar()
plt.title('Expected Recruitment Salary')
plt.xlabel('Salary Range')
plt.ylabel('Number')
plt.show()
