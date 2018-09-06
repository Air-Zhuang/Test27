# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 19:45'

'''
如何拆分含有多种分隔符的字符串
'''

import re

s='ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
print s

#传统方法split
# res=s.split(';')
# print res
# # print map(lambda x:x.split('|'),res)
# t=[]
# map(lambda x:t.extend(x.split('|')),res)
# print t
# res=t
# t=[]
# map(lambda x:t.extend(x.split(',')),res)
# print t
# res=t
# t=[]
# map(lambda x:t.extend(x.split('\t')),res)
# print t

#传统方法split使用循环
# def mySplit(s,ds):
#     res=[s]
#     for i in ds:
#         t = []
#         map(lambda x:t.extend(x.split(i)),res)
#         res=t
#     return [i for i in res if i]
# print mySplit(s,';|,\t')

#使用re.split()
print re.split(r'[;|,\t]+',s)