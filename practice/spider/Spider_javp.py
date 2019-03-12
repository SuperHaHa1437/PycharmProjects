from urllib import request
import requests
import re
from bs4 import BeautifulSoup
from selenium import webdriver


class SpiderJavp:
    url = 'https://javpreview.tumblr.com/'
    # root_pattern = '<section id="page">([\s\S]*?)</section>'
    root_pattern = '<h4 class="card-title m-t-0 m-b-10">([\s\S]*?)</h4>'
    # url = 'https://www.google.com'
    proxies = {
        'https': 'https://127.0.0.1:1087',
        'http': 'http://127.0.0.1:1087'
    }

    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    #     "Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}

    def __fetch_content(self):
        # opener = request.build_opener(request.ProxyHandler(SpiderJavp.proxies))
        # request.install_opener(opener)
        #
        # req = request.Request(SpiderJavp.url)
        # htmls = request.urlopen(req).read().decode('utf-8')

        # response = requests.get(SpiderJavp.url, proxies=SpiderJavp.proxies)
        # 本地读取网页
        tumblr_htmls = open('/Users/superhaha/Desktop/Rin Shiraishi.txt', 'r+', encoding='utf-8')

        return tumblr_htmls

    def __analysis(self,htmls):
        soup = BeautifulSoup(htmls, 'lxml')
        htmls = soup.prettify()

        root_html = re.findall(SpiderJavp.root_pattern, htmls)
        anchors = []
        # for html in root_html:
        #     # for href_link in soup.find_all('a'):
        #     #     anchors.append(href_link.get('href'))
        #     return anchors

    def __refine(self, anchors):
        f = open("/Users/superhaha/Desktop/origin_text.txt", 'w', encoding='utf-8')
        for anchor in anchors:
            anchor = re.findall('(https://t.umblr.com.*)', str(anchor))
            if (len(anchor) == 0):
                pass
            else:
                f.write(anchor[0]+'\n')
                print(anchor)



    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
        # self.__refine(anchors)


spidr_url = SpiderJavp()
spidr_url.go()
