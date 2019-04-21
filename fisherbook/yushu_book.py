"""
Created by 张 on 2019/3/27 
"""
__author__ = '张'

from httper import HTTP
from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword):
        url = cls.keyword_url.format(keyword)
        result = HTTP.get(url)
        return result


