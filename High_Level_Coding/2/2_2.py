# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/20 21:35'

from collections import namedtuple

'''
为每个元祖命名，提高程序可读性
'''
#使用枚举的方式
a,b,c,d =range(4)
print a
print b
print c
print d

#使用namedtuple
Stuent=namedtuple('StudentTuple',['name','age','sex'])
s1=Stuent('xiaoming',16,'male')
print s1
s2=Stuent(name='xiaohong',age=18,sex='female')
print s2
print s2.name