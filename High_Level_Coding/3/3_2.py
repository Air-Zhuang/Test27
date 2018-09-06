# _*_ coding: utf-8 _*_
__author__ = 'Air Zhuang'
__date__ = '2018/4/22 15:38'

'''
实现可迭代对象和迭代器对象
'''
import requests
from collections import Iterable,Iterator

# def getWeather(city):
#     r=requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
#     data=r.json()['data']['forecast'][0]
#     return '%s:%s,%s' % (city,data['low'],data['high'])
# print getWeather(u'北京')
# print getWeather(u'长春')

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0
    def getWeather(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])
    def next(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities
    def __iter__(self):
        return WeatherIterator(self.cities)

city=[u'北京',u'上海',u'广州',u'长春',u'青岛',u'济南',u'乌鲁木齐',u'海口',u'大连',u'大理',u'九江',u'石家庄']

wea=WeatherIterable(city)
for i in wea:
    print i