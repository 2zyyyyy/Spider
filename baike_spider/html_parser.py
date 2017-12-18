# coding:utf-8
from bs4 import BeautifulSoup
import urllib.parse
import re
class HtmlParser(object):
    
    def _get_new_urls(self, page_url, soup):
        # root_url/view/10812319.htm
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/view/\d/.htm"))
        for link in links:
            new_url = link['href']
            new_full_url=urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parse')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
