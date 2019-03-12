"""
Created by 张 on 2019/3/5 
"""
__author__ = '张'

from urllib import request
import urllib

# url = 'https://video2.fkvideo.cc/418cfc27a5724825923a5704d8ccc752.mp4'
class SpiderFK():
    headers = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'

    # def down_pic(self,url, path):
    #     try:
    #         req = request.Request(url, headers=SpiderFK.headers)
    #         data = request.urlopen(req).read()
    #         with open(path, 'wb') as f:
    #             f.write(data)
    #             f.close()
    #     except Exception as e:
    #         print(e)
    def down(self,url,path):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              SpiderFK.headers)]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, path)


spiderfk = SpiderFK()
spiderfk.down('https://video2.fkvideo.cc/418cfc27a5724825923a5704d8ccc752.mp4', '/Users/superhaha/Downloads/a.mp4')
