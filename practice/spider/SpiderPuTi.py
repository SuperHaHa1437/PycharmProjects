from urllib import request
import re


class SpiderPuTi():
    url = "http://www.theqi.com/buddhism/GL1/data/s02a.html"

    root_pattern = '<p class=b>([\s\S]*?)</p>'
    original_pattern = '【[\s\S]{0,}】'

    def __fetch_content(self):
        r = request.urlopen(SpiderPuTi.url)
        htmls = r.read()
        htmls = str(htmls, encoding='Big5')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(SpiderPuTi.root_pattern, htmls)
        anchors = []
        for html in root_html:
            original_text = re.findall(SpiderPuTi.original_pattern, html)
            anchors.append(original_text)

        return anchors

    def __show(self, anchors):
        for anchor in anchors:
            print(anchor)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__show(anchors)


spider = SpiderPuTi()
spider.go()
