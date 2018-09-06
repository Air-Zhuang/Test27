# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/5 19:37'

import requests
BASE_URL='https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASE_URL,end_point])
def basic_auth():
    response=requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
    print response.text
    print response.request.headers
def basic_oauth():
    headers={'Authorization':'token 6c4621bae1dbdc08520199f7112151f8b700cfa1'}
    response=requests.get(construct_url('user/emails'),headers=headers)
    print response.request.headers
    print response.text
    print response.status_code

from requests.auth import AuthBase
class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token=token
    def __call__(self,r):
        r.headers['Authorization']=' '.join(['token',self.token])
        return r
def oauth_upgrade():
    auth=GithubAuth('6c4621bae1dbdc08520199f7112151f8b700cfa1')
    response=requests.get(construct_url('user/emails'),auth=auth)
    print response.request.headers
    print response.text
    print response.status_code

oauth_upgrade()