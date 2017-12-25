# coding:utf-8

import requests
from bs4 import BeautifulSoup

"""
    访问煎蛋画廊主页，获取html文本
    分析html文本，找出所有图片的html特征
    解析html代码，拿到所有图片的src
    通过src去下载图片
"""
headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36'
            'KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}  # 通过修改http headers 的user agent,达到将求情伪装成是来自普通chrome浏览器的请求


def download_file(url):
    print('Download %s' %url)
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True, headers=headers)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename

url = 'http://jandan.net/drawings'
soup = BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser')


def valid_img(src):
    return src.endswith('jpg') and 'img.jandan.net' in src

for img in soup.find_all('img', src=valid_img):
    src = img['src']
    if not src.startswith('http'):
        src = 'http:' + src
    download_file(src)

