# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/24 20:36'

'''
在python中:property()方法整合了get方法，set方法
可管理的对象属性
'''

#使用property函数为类创建可管理属性，fget/fset/fdel对应相应访问属性

from math import pi

class Circle(object):
    def __init__(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    def setRadius(self,value):
        if not isinstance(value,(int,long,float)):
            raise ValueError('wrong type.')
        self.radius=float(value)
    def getArea(self):
        return self.radius**2*pi
    R=property(getRadius,setRadius) #整合set和get

c=Circle(3.2)
print c.getArea()
print

print c.R #相当于get
c.R=5.2   #相当于set
print c.R