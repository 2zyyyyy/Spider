# coding:utf-8

from baike_spider import html_downloader, html_outputer, html_parser, url_manager


class SpiderMain(object):
    def __init__(self):
        '''
            url管理器
            url下载器
            url解析器
            url输出器
        '''
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):  # 爬虫的调度程序
        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():  # 当URL管理器中存在URL的时候启动循环
            count = 1
            '''
                获取到待爬取的URL
                启动下载器来下载这个页面 存储在html_cont  
                调用解析器解析页面 得到新的URL列表和数组
                将新的url数据补充进url管理器同时进行数据的收集
                输出收集好的数据
            '''
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except:
                print('craw failed!')

        self.outputer.output_html()  # 输出


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
