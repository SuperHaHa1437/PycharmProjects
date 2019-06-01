"""
Created by 张 on 2019/3/29
"""
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from . import web

__author__ = '张'


# 视图函数
@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify(form.errors)
