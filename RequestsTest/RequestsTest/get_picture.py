# _*_ coding: utf-8 _*_
# __author__ = 'Air Zhuang'
# __date__ = '2018/6/4 22:51'

import requests
def download_image():
    url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1528133947412&di=643ef1a99d58943de28f9a682a15c833&imgtype=0&src=http%3A%2F%2Fimage.mamicode.com%2Finfo%2F201802%2F20180206122017476065.png'
    response=requests.get(url=url,stream=True)
    with open('demo.png','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
def download_image_upgrade():
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1528133947412&di=643ef1a99d58943de28f9a682a15c833&imgtype=0&src=http%3A%2F%2Fimage.mamicode.com%2Finfo%2F201802%2F20180206122017476065.png'
    from contextlib import closing
    with closing(requests.get(url=url,stream=True)) as response:
        with open('demo2.png', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)
if __name__ == '__main__':
    # download_image()
    download_image_upgrade()