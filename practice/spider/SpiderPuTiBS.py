from bs4 import BeautifulSoup
from urllib import request
import re


class SpiderPuTiBS():
    url = "http://www.theqi.com/buddhism/GL1/data/s22b.html"
    root_pattern = '<p class=b>([\s\S]*?)</p>'
    original_pattern = '【[\s\S]{0,}】'

    def __fetch_content(self):
        r = request.urlopen(SpiderPuTiBS.url)
        htmls = r.read()
        htmls = str(htmls, encoding='Big5')
        return htmls

    def __analysis(self, htmls):
        soup = BeautifulSoup(htmls, 'lxml')

        anchors = []
        # 分别获取 属性 class 值为 a b 的内容
        for html in soup.find_all('p', attrs={'class': 'a', 'class': {'a', 'b'}}):
            # 由于 soup 返回的对象不是 str,在 re.findall 需要以 str 或者字节的参数格式传入
            html = str(html)
            html = re.findall(SpiderPuTiBS.original_pattern, html)
            anchors.append(html)

        return anchors

    def __show(self, anchors):
        f = open("/Users/superhaha/Desktop/origin_text.txt", 'w', encoding='utf-8')
        for anchor in anchors:
            f.write(anchor[0] + "\n")
            print(anchor)

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__show(anchors)


spider = SpiderPuTiBS()
spider.go()
