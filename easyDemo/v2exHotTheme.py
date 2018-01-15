# coding:utf=8
import requests
from bs4 import BeautifulSoup

"""
    层级遍历
    访问v2ex主页，获取html文本
    分析html文本，找出待获取内容的特征
    解析html代码，根据特征拿出目标内容
    打印这些内容
"""


def add(a, b):
    return a + b

url = "https://www.v2ex.com"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

for span in soup.find_all('span', class_='item_hot_topic_title'):
    print(span.find('a').text, url + span.find('a')['href'])
    # 这里可以用urllib.parse 的urljoin方法拼接地址
"""
    1、for span in soup.find_all('span', class_='item_hot_topic_title'): 
    遍历所有的class=item_hot_topic_title的span。注意是class_，不是class，因为class是python的关键字，所以后面要加个尾巴，防止冲突
    
    2、span.find('a').text：层级遍历，先找到span，再从span下找到a，这是常用套路

    3、span.find('a')['href']：获取href属性，在bs4里，我们可以通过[attribute_name]的方式来获取元素的属性
"""
