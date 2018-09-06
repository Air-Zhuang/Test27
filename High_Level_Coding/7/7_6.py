# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 22:17'

'''
使用描述符对实例属性做类型检查
'''
class Attr(object):
    def __init__(self,name,type_):
        self.name=name
        self.type_=type_
    def __get__(self, instance, cls):
        return instance.__dict__[self.name]   #使传进来的属性可以变成Person的类属性
    def __set__(self, instance, value):
        if not isinstance(value,self.type_):
            raise TypeError('expected an %s' % self.type_)
        instance.__dict__[self.name]=value  #使传进来的属性可以变成Person的类属性
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Person(object):
    name=Attr('name',str)
    age=Attr('age',int)
    height=Attr('height',float)

p=Person()
p.name='Bob'
print p.name

# p.age='17'    #这里会抛出类型不匹配的异常