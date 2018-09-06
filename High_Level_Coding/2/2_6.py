# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 13:44'

'''
如何让字典保持有序
'''

from random import randint
from time import time
from collections import OrderedDict

starttime=time()
players=list('ABCDEFGH')
d=OrderedDict()
for i in range(len(players)):
    raw_input()
    p=players.pop(randint(0,7-i))
    endtime=time()
    print i+1,p,endtime-starttime
    d[p]=(i+1,endtime-starttime)

print
for i in d:
    print i,d[i]


