"""
Created by 张 on 2019/3/29
"""
from flask import jsonify, request
from flask import Blueprint
from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = '张'

web = Blueprint('web', __name__)


# 视图函数
@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
