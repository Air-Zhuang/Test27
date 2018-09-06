# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 18:57'

'''
在一个for语句中迭代多个可迭代对象
'''

from random import randint
from itertools import chain

#并行
chinese=[randint(60,100) for i in range(10)]
math=[randint(60,100) for i in range(10)]
english=[randint(60,100) for i in range(10)]
total=[]
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print total

#串行:使用itertools.chain()方法
c1=[randint(60,100) for i in range(5)]
c2=[randint(60,100) for i in range(4)]
c3=[randint(60,100) for i in range(3)]
c4=[randint(60,100) for i in range(6)]
count=0
for i in chain(c1,c2,c3,c4):
    if i>=90:
        count+=1
print count