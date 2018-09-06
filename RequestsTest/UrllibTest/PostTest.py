# -*- coding: utf8 -*-
import urllib
import urllib2

url="http://xapi.kybyun.com/user/login"
header={}

data={}
data['appchg']='AppStore'
data['apptype']='21'
data['appver']='2.1.3.1'
data['email']='mushishi01'
data['isbind']='0'
data['passwd']='111111'
data['sysdev']='iPhone 6 Plus'
data['sysver']='9.3'
data['uuid']='6ff7563dbd47c8077905c3920bc0d8b3'
data=urllib.urlencode(data)

req=urllib2.Request(url,data,header)
ResponseStr=urllib2.urlopen(req)
ResponseStr=ResponseStr.read()
ResponseStr=ResponseStr.decode("unicode_escape")
print(ResponseStr)











