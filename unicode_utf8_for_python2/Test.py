# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'

s="abc"
su=u"abc"
print s.encode("utf8")
print su.encode("utf8")

s1="我用python2"
su1=u"我用python2"
# print s1.encode("utf8")#报错
print su1.encode("utf8")#这里用encode,su1必须是unicode编码

#将其他编码变成unicode编码,
# window下python2的编码是GB2312(控制台)，pycharm下的编码是gbk，linux为utf-8,所以这里填gbk
print s1.decode("gbk").encode("utf-8")