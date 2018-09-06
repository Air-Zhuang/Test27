# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/5/31 21:47'

import json
import requests

URL='https://api.github.com'

URL_IP='http://httpbin.org/ip'
URL_GET='http://httpbin.org/get'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def get_demo():
    print "get:"
    response=requests.get(URL_IP)
    print response.headers
    print response.text

    params = {'param1': 'hello', 'param2': 'world'}
    response2 = requests.get(URL_GET,params=params)
    print response2.headers
    print response2.status_code
    print response2.reason
    print response2.json()

def request_method():
    response=requests.get(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'))
    print better_print(response.text)

def params_request():
    response=requests.get(build_uri('users'),params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url
def json_request():
    response=requests.patch(build_uri('user'),auth=('imoocdemo','imoocdemo123'),json={'name':'babymooc2','email':'hello-world@imooc.org'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code
def post_request():#自定义Request
    response=requests.post(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),json=['helloworld@github.com'])
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code

def hard_requests():
    from requests import Request,Session
    s=Session()
    headers={'User-Agent':'fake1.3.4'}
    req=Request('GET',build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),headers=headers)
    prepped=req.prepare()
    print prepped.body
    print prepped.headers

    resp=s.send(prepped)
    print resp.status_code
    print resp.request.headers
    print resp.text

if __name__ == '__main__':
    # get_demo()
    # request_method()
    # params_request()
    # json_request()
    post_request()
    # hard_requests()