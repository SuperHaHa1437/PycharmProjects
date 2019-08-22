"""
Created by 张 on 2019/8/15 
"""
__author__ = '张'


# 图书 book 的 viewmodel 层,用于视图函数层解析数据以返回给客户端
# 具体的单一数据处理封装在BookViewModel里
class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    # 在搜索书籍页面里，需要将每一条结果的作者，出版社，价格在一行展示，并以” / “分割。
    # @property装饰器可以让我们把一个方法当做一个属性来使用
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        return '/'.join(intros)


# 处理 yushu_book 返回的多本图书数据集合
class BookCollection:
    def __init__(self):
        """
        初始化三个实例变量
        """
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        """
        解析从 yushu_book 拿到的书籍数据,提取所需要的.
        :param yushu_book: yushu_book 对象获取到的 API 数据
        :param keyword: 搜索关键字
        """
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword




class _BookViewModel:
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
