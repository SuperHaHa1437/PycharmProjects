"""
Created by 张 on 2019/8/5 
"""
from app.libs.httper import HTTP
from flask import current_app

__author__ = '张'


# 鱼书业务查询
class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """
        isbn 搜索方法
        :param isbn: 搜索 isbn
        :return: 返回请求到的结果
        """
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        """
        关键字搜索方法
        :param keyword: 搜索关键字
        :param page: 页数,默认值 1
        :return: 返回请求到的结果
        """
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        """
        解析 isbn 搜索的单本书籍数据
        :param data: API 请求原始数据
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """
        解析关键字搜索的多本书籍数据
        :param data: API 请求原始数据
        """
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        """

        :param page: 搜索的结果有多少页,每 15 个结果为一页
        :return: 返回每一页的从第几个结果开始返回,比如第一页的十五个结果,从第 0 个开始也就是第一个.
        """
        return (page - 1) * current_app.config['PER_PAGE']
