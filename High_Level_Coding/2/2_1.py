# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/20 16:30'

from random import randint

'''
如何在列表，字典，集合中根据条件筛选数据
'''

#传统办法
data=[1,5,-3,-2,6,0,9]
print data
res=[]
for i in data:
    if i>0:
        res.append(i)
print "传统方法:",res

#列表：filter函数
data2=[randint(-10,10) for i in range(10)]
print data2
print "过滤器方法:",filter(lambda x:x>=0,data2)

#列表：列表列表解析
print "列表解析：",[i for i in data2 if i>=0]

#字典列表解析
data3={k:randint(60,100) for k in range(1,21)}
print data3
print "字典列表解析",{k:v for k,v in data3.iteritems() if v>=90}

#集合列表解析
s=set(data2)
print "集合列表解析",{i for i in s if i%3==0}
