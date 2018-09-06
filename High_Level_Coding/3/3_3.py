# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 16:32'

'''
实现生成器函数实现可迭代对象：yield
'''

# def f():
#     print 'in f(),1'
#     yield 1
#     print 'in f(),2'
#     yield 2
#     print 'in f(),3'
#     yield 3

class PrimeNumbers(object):
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrime(self,k):
        if k<2:
            return False
        for i in xrange(2,k):
            if k%i==0:
                return False
        return True
    def __iter__(self):
        for i in xrange(self.start,self.end):
            if self.isPrime(i):
                yield i

for i in PrimeNumbers(1,100):
    print i