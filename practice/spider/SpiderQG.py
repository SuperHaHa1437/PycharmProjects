import urllib
from bs4 import BeautifulSoup
from urllib import request
import re


class SpiderQG():
    url = "http://www.3gmfw.cn/article/html2/2019/05/25/465173_2.html"

    # url = "https://bltang.cc/6745.html"

    root_pattern = '<div class="mainNewContent NewsContent" id="mainNewContent">([\s\S]*?)</div>'
    original_pattern = '【(.*)】'
    headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    def __fetch_content(self):
        url_list = []
        textlist = []
        for i in range(1, 35):
            if i == 1:
                url = 'http://www.3gmfw.cn/article/html2/2019/05/25/465173.html'
            else:
                url = 'http://www.3gmfw.cn/article/html2/2019/05/25/465173_' + str(i) + '.html'
            url_list.append(url)

        for url in url_list:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})
            r = request.urlopen(req)
            htmls = r.read()
            htmls = str(htmls, encoding='GBK')
            soup = BeautifulSoup(htmls, 'lxml')
            html_text = str(soup.find(id='mainNewsContent'))
            textlist.append(html_text)
        print(textlist)

        f = open("/Users/superhaha/Desktop/origin_text.txt", 'w+', encoding='utf-8')
        f.write(str(textlist))
        # for t in textlist:
        #     f.write(t+'\n')
        #     print(t)


    def __analysis(self, htmls):
        soup = BeautifulSoup(htmls, 'lxml')
        html_text = str(soup.find_all('p'))


    def __show(self, anchors):
        for anchor in anchors:
            print(anchor)

    def go(self):
        self.__fetch_content()
        # htmls = self.__fetch_content()
        # anchors = self.__analysis(htmls)
        # self.__show(anchors)


spider = SpiderQG()
spider.go()
