# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 17:36'

'''
如何派生内置不可变类型并修改实例化行为
'''

class IntTuple(tuple):  #跟原本的tuple是一样的
    def __init__(self,iterable):
        super(IntTuple,self).__init__(iterable)

#使用__new__方法
class IntTuple(tuple):
    def __new__(cls, iterable):
        g=(x for x in iterable if isinstance(x,int) and x>0)
        return super(IntTuple,cls).__new__(cls,g)
    def __init__(self,iterable):
        super(IntTuple,self).__init__(iterable)

t=IntTuple([1,-1,'abc',6,['x','y'],3])
print t