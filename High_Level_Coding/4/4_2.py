# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 20:44'

'''
如何判断字符串a是否以字符串b开头或结尾
'''

import os,stat
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print path
print os.listdir(path)
print os.stat(path+'\\test\\4_2.txt')
print oct(os.stat(path+'\\test\\4_2.txt').st_mode)   #oct()转换成八进制
#修改文件权限
os.chmod(path+'\\test\\4_2.txt',os.stat(path+'\\test\\4_2.txt').st_mode | stat.S_IXUSR) #修改文件权限
print oct(os.stat(path+'\\test\\4_2.txt').st_mode)
print

#判断文件以字符串开头或结尾   str.startswith() str.endswith()
l=['e.py','g.sh','d.java','h.c','f.cpp','a.sh','c.h','b.py']
# s='g.sh'
# print s.endswith(('.sh','.py','.txt'))#必须是字符串或是元组
print [name for name in l if name.endswith(('.sh','.py'))]

