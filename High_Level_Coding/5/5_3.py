# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/23 20:08'

'''
如何设置文件的缓冲
'''

import os
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#全缓冲,buffering为缓冲区域大小2048
# f=open(path+"\\test\\5_3.txt",'w',buffering=2048)
# f.write('+'*2048)

#行缓冲，buffering=1
# f=open(path+"\\test\\5_3.txt",'w',buffering=1)
# f.write('aaa')
# f.write('\n')

#无缓冲，buffering=0
f=open(path+"\\test\\5_3.txt",'w',buffering=0)
