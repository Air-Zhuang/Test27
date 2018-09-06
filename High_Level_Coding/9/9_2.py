# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/27 23:07'

'''
如何为被装饰的函数保存元数据
使用标准库functools中的装饰器wraps装饰内部包裹函数，
可以指定将原函数的某些属性，更新到包裹函数上面
'''

def f(a,b=1,c=[]):
    '''f function'''
    return a*2
def f2():
    a=2
    return lambda k:a**k

print f.__name__    #函数名
print f.__doc__     #函数注释
print f.__module__  #函数所属模块
print f.__defaults__#函数默认参数
g=f2()
print g.__closure__[0].cell_contents    #闭包

from functools import wraps

def mydecorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        '''wrapper function'''
        print 'In wrapper'
        func(*args,**kwargs)
    return wrapper

@mydecorator
def example():
    '''example function'''
    print 'In example'

print example.__name__
print example.__doc__