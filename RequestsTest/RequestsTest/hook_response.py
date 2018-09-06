# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/5 19:17'

import requests
def get_key_info(response,*args,**kwargs):
    print response.headers['Content-Type']
def method():
    requests.get('https://api.github.com',hooks=dict(response=get_key_info))

method()