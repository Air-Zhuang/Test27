# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/20 21:59'

from random import randint
from collections import Counter
import os,re

path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''
统计序列中元素的出现频率
'''

#使用dict.fromkeys方式
data1=[randint(0,20) for i in range(30)]
print data1
dict1=dict.fromkeys(data1,0)
print dict1
for i in data1:
    dict1[i]+=1
print dict1

#用collections.Counter选出数量前三
dict2=Counter(dict1)
print dict2.most_common(3)

print

txt=open(path+"\\test\\test.txt").read()
txt2=re.split('\W+',txt)
print txt2
txt3=Counter(txt2)
print txt3
print txt3.most_common(3)


