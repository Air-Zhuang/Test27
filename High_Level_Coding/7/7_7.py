# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 22:39'

'''
(处理循环引用，进行垃圾回收)
如何在环状数据结构中管理内存
'''
import weakref

class Data(object):
    def __init__(self,value,owner):
        self.owner=weakref.ref(owner) #使用弱引用，这样不会增加Node的引用计数
        self.value=value
    def __str__(self):
        return "%s's data,value is %s" % (self.owner(),self.value)
    def __del__(self):
        print 'in Data.__del__'
class Node(object):
    def __init__(self,value):
        self.data=Data(value,self)
    def __del__(self):
        print 'in Node.__del__'

node=Node(100)
del node    #删除引用成功
