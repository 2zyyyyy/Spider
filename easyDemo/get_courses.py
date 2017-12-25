# coding:utf-8

import requests
from bs4 import BeautifulSoup

url = 'http://www.itest.info/courses'
# #获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup 属于固定套路
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# 遍历h4
for course in soup.find_all('h4'):
    # 打印出课程名称
    print(course.text)