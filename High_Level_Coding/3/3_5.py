# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 18:21'

'''
对迭代器做切片操作
'''

import os
from itertools import islice
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#传统方法，耗内存
# f=open(path+"\\test.txt")
# lines=f.readlines()
# print lines
# print lines[2:5]

#使用迭代器:itertools.islice()
# f.seek(0)#使文件指针回到头部
# for i in f:
#     print i

# f.seek(0)
# for i in islice(f,2,5):
#     print i

l=range(10)
print l
t=iter(l)
for i in islice(t,2,5):
    print i
print
for i in t:#islice会抛弃已迭代的部分，所以再次迭代需要重新申请对象
    print i
