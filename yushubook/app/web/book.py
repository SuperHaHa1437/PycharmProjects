"""
Created by 张 on 2019/8/5 
"""
import json

from flask import Blueprint, jsonify, request, flash, render_template

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
    7.通过 json.dumps 返回拿到的数据,并通过 Python 内置变量__dict__序列化对象以拿到对象所有属性组成的字典
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
        # return json.dumps(books, default=lambda o: o.__dict__)
    else:
        flash('搜索的关键字不符合要求,请重新输入关键字 ')

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    """
    书籍详情页面,数据从 yushu_book 中拿到,因为是通过指定书籍详情页面,所以用 search_by_isbn
    通过 BookViewModel 处理 yushu_book 中的数据,只需要处理单本的数据,所以使用 BookViewModel 即可,不需要 BookCollection 处理集合数据
    BookViewModel 处理的是 yushu_book 对象下 books 属性即列表下的第一个元素,封装到 first 方法中,用 @property 将 first 方法作为属性调用
    :param isbn: 通过 isbn 跳转到指定书籍详情页面
    :return: 返回书籍详情页面
    """
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])
