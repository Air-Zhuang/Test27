# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 19:46'

'''
创建大量实例节省内存
'''
class Player(object):   #传统，占内存
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level

class Player2(object):  #省内存
    __slots__ = ['uid','name','stat','level']
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level
p1=Player('001','Jim')
p2=Player2('001','Jim')
print set(dir(p1))-set(dir(p2)) #传统比省内存之间多的属性，主要占内存的是__dict__