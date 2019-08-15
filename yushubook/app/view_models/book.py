"""
Created by 张 on 2019/8/15 
"""
__author__ = '张'


# 图书 book 的 viewmodel 层,用于视图函数层解析数据以返回给客户端
class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        """
        isbn 搜索返回单本图书的数据
        :param data: API返回的数据源
        :param keyword: 搜索的关键字,因为数据源没有此参数,所以根据搜索的关键字将其传入
        :return: 返回裁切好的数据
        """
        # 获取到的图书数据分为三类提供给客户端
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        # 如果有获取到数据
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """

        :param data: API返回的数据源
        :param keyword: 搜索的关键字,因为数据源没有此参数,所以根据搜索的关键字将其传入
        :return: 返回一组图书的数据
        """
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """
        裁剪原数据,拿到需要的数据
        :param data: 原始数据
        :return: 返回裁切好的需要用到的数据
        """
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
