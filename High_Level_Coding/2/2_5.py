# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 12:07'

from random import randint,sample

'''
如何快速找到多个字典中的公共键
'''
#第一种方式：传统
first={k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
second={k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
third={k:randint(1,4) for k in sample('abcdefg',randint(3,6))}
print first;print second;print third
res=[]
for i in first:
    if i in second and i in third:
        res.append(i)
print res

#第二种方式：dict.viewkeys()
print
print first.viewkeys() & second.viewkeys() & third.viewkeys()

#第三种方式：viewkeys()+map()+reduce()
print
res2=map(dict.viewkeys,[first,second,third])
print res2
print reduce(lambda a,b:a & b,res2)


