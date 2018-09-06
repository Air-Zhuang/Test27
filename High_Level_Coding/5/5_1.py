# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 17:59'

'''
如何读取文本文件
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

a=u'你好'
a1=a.encode('utf8')
print a.encode('gbk')
print a1.decode('utf8')
print
#python2  写入读取
f=open(path+"\\test\\5_1.txt",'w')
s=u'你好python2'
f.write(s.encode('utf8'))
f.close()
f=open(path+"\\test\\5_1.txt",'r')
t=f.read()
print t.decode('utf8')
f.close()

#python3  写入读取
# ff=open(path+"\\5_1.txt",'wt',encoding='utf8')
# ff.write('你好python3')
# ff.close()
# ff=open(path+"\\5_1.txt",'rt',encoding='utf8')
# ss=ff.read()
# print ss