# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 15:33'

'''
迭代器的原理
'''
a=[1,2,3,4,5]
b=iter(a)
print b.next()
print b.next()
print b.next()
print b.next()
print b.next()