# -*- coding: utf-8 -*-
import urllib
import urllib2

url="http://reg.haibian.com/login/ajax_login"
data={}
data['loginname']='student08@qq.com'
# data['password']='96e79218965eb72c92a549dd5a330112'
data['password']='111111'
data=urllib.urlencode(data)
request=url+'?'+data

requestResponse=urllib2.urlopen(request)
ResponseStr=requestResponse.read()
ResponseStr=ResponseStr.decode("unicode_escape")
print(ResponseStr)















