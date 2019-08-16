"""
Created by 张 on 2019/8/5 
"""
from flask import Blueprint, jsonify, request, flash

from app.forms.bookforms import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from . import web

__author__ = '张'


# 将视图函数注册到蓝图中,在 app.__init__中将蓝图注册到 app 中
@web.route('/book/search')
def search():
    """
    请求流程:
    1.外部请求 search 视图函数,请求参数校验成功
    2.判断请求是 isbn or 关键字
    3.yushu_book 请求 API 获取数据
    4.yushu_book 内获取的数据存储在类中(实例变量 total,books),根据不同的请求关键字存储数据
    5.将 yushu_book(此时类中有API 请求回已存储好的数据) 传递至 BookCollection 的实例的实例方法fill中
    6.在 BookCollection 中拿到所需要的数据
    :return: 返回搜索的结果
    """
    # 校验请求的参数
    form = SearchForm(request.args)
    # 实例化 book 的 viewmodel,以解析请求的数据
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        # 判断是 isbn 请求 or 关键字请求
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return jsonify(books)
    else:
        flash('搜索的关键字不符合要求,请重新输入关键字 ')
