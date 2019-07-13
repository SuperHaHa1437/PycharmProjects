import urllib
from urllib import request
import re


class SpiderQG():
    url = "http://www.3gmfw.cn/article/html2/2019/05/25/465173.html"
    # url = "https://bltang.cc/6745.html"

    root_pattern = '<p class=b>([\s\S]*?)</p>'
    # root_pattern = '<p class=b>(.*)</p>'
    original_pattern = '【(.*)】'
    headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    def __fetch_content(self):
        req= urllib.request.Request(SpiderQG.url,headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'})
        r = request.urlopen(req)
        htmls = r.read()
        htmls = str(htmls, encoding='GBK')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(SpiderQG.root_pattern, htmls)
        anchors = []
        for html in root_html:
            original_text = re.findall(SpiderQG.original_pattern, html)
            anchors.append(original_text)

        return anchors

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
