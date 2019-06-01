"""
Created by 张 on 2019/3/22 
"""
__author__ = '张'

import requests

class HTTP:
    # 由于用不到普通实例方法的 self,所以改为静态方法
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        # 判断搜索后的结果的状态码.200以外才是搜索成功
        if r.status_code != 200:

            return {} if return_json else ''
        return r.json() if return_json else r.text


