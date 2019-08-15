"""
Created by 张 on 2019/8/5 
"""
__author__ = '张'

import requests


# 网络请求工具类
class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
