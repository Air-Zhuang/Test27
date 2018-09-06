# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/20 23:08'

from random import randint

'''
如何根据字典中值的大小，对字典中的项排序
'''
#使用zip
dict1={i:randint(0,100) for i in 'abcdef'}
print dict1
dict2=sorted(zip(dict1.values(),dict1.keys()))
print dict2
#使用sorted的key属性
print sorted(dict1.items(),key=lambda x:x[1])
