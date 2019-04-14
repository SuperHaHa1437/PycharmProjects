"""
Created by 张 on 2019/3/29 
"""
from flask import jsonify
from YuShu import YuShuBook
from helper import is_isbn_or_key
from . import web

__author__ = '张'




# 视图函数
@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
