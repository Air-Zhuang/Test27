# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 20:23'

'''
如何处理二进制文件
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import struct,array
print struct.unpack('h','\x01\x02')

f=open(path+"\\test\\music.wav",'rb')
info=f.read(44)
print info

f.seek(0,2) #将指针移动到队尾，用tell查看当前指针位置，从而得知文件大小
size=f.tell()
print size

n=(size-44)/2
buf=array.array('h',(0 for i in xrange(n)))

f.seek(44)
f.readinto(buf)

for i in xrange(n): #将音量缩小
    buf[i]/=8

f2=open(path+"\\test\\music2.wav",'wb')
f2.write(info)
buf.tofile(f2)
f2.close()



