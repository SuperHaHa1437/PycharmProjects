from bs4 import BeautifulSoup
from urllib import request
import re


class SpiderPuTiBS():
    url = 'http://www.theqi.com/buddhism/GL1/data/s25b.html'

    # 匹配括号内的文字
    original_pattern = '【.*】'
    # 过滤括号内文字的一些网页标签
    char_filter_pattern = '([a-zA-Z0-9()<>="/\s]+)'

    def __fetch_content(self):
        r = request.urlopen(SpiderPuTiBS.url)
        htmls = r.read().decode('Big5')
        return htmls

    def __analysis(self, htmls):
        soup = BeautifulSoup(htmls, 'lxml')

        anchors = []
        # 分别获取 属性 class 值为 a b 的内容
        for html in soup.find_all('p', attrs={'class': {'a', 'b'}}):
            # 过滤掉某些网页标签
            html = re.sub(SpiderPuTiBS.char_filter_pattern, '', str(html))
            # 由于 soup 返回的对象不是 str,在 re.findall 需要以 str 或者字节的参数格式传入
            html = re.findall(SpiderPuTiBS.original_pattern, str(html))
            anchors.append(html)

        return anchors

    def __show(self, anchors):
        f = open("/Users/superhaha/Desktop/origin_text.txt", 'w+', encoding='utf-8')
        for anchor in anchors:
            if len(anchor) == 0:
                print('\033[5;33m 有一组数据初始规则匹配失败 \033[0m')
            else:
                f.write(anchor[0] + "\n")
                print(anchor[0])

        # 列表推导式
        # [f.write(anchor[0] + "\n") for anchor in anchors if len(anchor) != 0]
        # [print(anchor[0]) for anchor in anchors if len(anchor) != 0]

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__show(anchors)


spider = SpiderPuTiBS()
spider.go()
