# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 22:48'

'''
如何去掉字符串中不需要的字符
'''

import re
import string

#使用str.strip()
s1='   abc   123   '
s2='+++abc---'
print s1.strip()
print s2.strip('+-')
print

#切片加拼接
s3='abc:123'
print s3[:3]+s3[4:]
print

#使用str.replace()(只能替换一个) re.sub()
s4='\tabc\t123\txyz\ropq\r'
print re.sub('[\t\r]','',s4)
print

#使用str.translate()
s5='abc564654xyz'
print s5.translate(string.maketrans('abcxyz','xyzabc'))
print s4.translate(None,'\t\r')