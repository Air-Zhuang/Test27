# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/4 22:32'

import requests
response=requests.get('https://api.github.com')
print "status_code:",response.status_code
print "reason:",response.reason
print "headers:",response.headers
print "url:",response.url
print "history:",response.history
print "elapsed:",response.elapsed
print "request:",response.request
print "request.headers:",response.request.headers
print "encoding:",response.encoding
print "raw:",response.raw
print "content:",response.content
print "text:",response.text
print "json():",response.json()