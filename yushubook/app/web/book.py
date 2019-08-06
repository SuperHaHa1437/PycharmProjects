"""
Created by 张 on 2019/8/5 
"""
from flask import Blueprint, jsonify

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

__author__ = '张'

web = Blueprint('web', __name__)


# 将视图函数注册到蓝图中,在 app.__init__中将蓝图注册到 app 中
@web.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
