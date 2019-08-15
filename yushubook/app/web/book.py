"""
Created by 张 on 2019/8/5 
"""
from flask import Blueprint, jsonify, request, flash

from app.forms.bookforms import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from . import web

__author__ = '张'


# 将视图函数注册到蓝图中,在 app.__init__中将蓝图注册到 app 中
@web.route('/book/search')
def search():
    """

    :return: 返回搜索的结果
    """
    form = SearchForm(request.args)

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        flash('搜索的关键字不符合要求,请重新输入关键字 ')
