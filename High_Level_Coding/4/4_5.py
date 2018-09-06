# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 22:27'

'''
如何对字符串进行左，居中，右对齐
'''
#使用str.ljust() str.rjust() str.center()
a='abc'
print a.ljust(20,'=')
print a.rjust(20)
print a.center(20,'+')
print
#使用format()方法
print format(a,'<20')
print format(a,'>20')
print format(a,'^20')
print

d={
    'asd':626,
    'dhfdgh':566416,
    'asdd':5848,
    'sdfasdf':64654.11,
    'fasdf':54151.4154
}
m=max(map(len,d.keys()))
for i in d:
    print i.ljust(m),':',d[i]
