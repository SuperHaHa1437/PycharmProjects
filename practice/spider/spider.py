from urllib import request
import re


class Spider():
    # 类变量
    url = 'https://bbs.52waha.com/'
    # url = "http://www.theqi.com/buddhism/GL1/data/s22b.html"

    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_patten = '</i>([\s\S]*?)</span>'
    number_patten = '<span class="video-number">([\s\S]*?)</span>'


    # 实例方法,参数默认 self
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        # 熊猫 TV
        htmls = str(htmls, encoding='gbk')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_patten, html)
            number = re.findall(Spider.number_patten, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank + 1) + ' : ' +
                  anchors[rank]['name'] + '--->' +
                  anchors[rank]['number'] + '人')

    def go(self):
        htmls = self.__fetch_content()
        # anchors = self.__analysis(htmls)/
        # anchors = list(self.__refine(anchors))
        # anchors = self.__sort(anchors)
        # self.__show(anchors)


spider = Spider()
spider.go()
