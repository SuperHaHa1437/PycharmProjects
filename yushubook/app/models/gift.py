"""
Created by 张 on 2019/8/20 
"""
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func

from app.spider.yushu_book import YuShuBook

__author__ = '张'


# 礼物模型类
class Gift(Base):
    id = Column(Integer, primary_key=True)
    # user 需要关联 User 模型
    user = relationship('User')
    # 拿到用户的唯一标识,也是 User模型类下的 id
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    """
    为什么要定义成类方法
    
    对象代表一个礼物，是具体的
    类代表礼物这个事物，他是抽象的，不是具体的一个
    """

    @classmethod
    def recent_gift(cls):
        """
        首页会显示最近的赠送书籍列表。这个列表有三个限制条件：
        1. 数量不超过 30
        2. 按照时间倒序排列，最新的排在最前面
        3. 去重，同一本书籍的礼物不重复出现
        :return:
        """
        recent_gift = Gift.query.filter_by(
            launched=False).order_by(
            desc(Gift.create_time)).distinct().limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift

    @classmethod
    def get_user_gift(cls, uid):
        """
        查询某个用户下所有的礼物
        过滤条件: uid,launched(未交易)
        :param uid:用户 id
        :return:返回所有的符合查询条件的礼物模型
        """
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """
        在Gift模型中,查询对应 isbn 在心愿清单中的数量
        :param isbn_list: Gift模型中所有 isbn 集合
        func.count() 数量总数
        查询条件:Wish 的总数,Wish的 isbn
        过滤条件:未交易,Wish的 isbn 在 Gift 的 isbn_list 中,未删除
        分组条件:Wish isbn
        :return:isbn 对应数量字典
        """
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1
        ).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        """
        处理从拿 isbn 编号去 YushBook 可去查询出书籍的详情信息
        :return:
        """
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
