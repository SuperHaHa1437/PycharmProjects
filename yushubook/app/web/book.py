"""
Created by 张 on 2019/8/5 
"""
from flask import Blueprint, jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web

__author__ = '张'


# 将视图函数注册到蓝图中,在 app.__init__中将蓝图注册到 app 中
@web.route('/book/search')
def search():
    q = request.args['q']
    page = request.args['page']
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
