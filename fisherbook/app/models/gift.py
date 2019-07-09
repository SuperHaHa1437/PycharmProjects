"""
Created by 张 on 2019/6/30 
"""
from flask import current_app

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

__author__ = '张'

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationship
from collections import namedtuple

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        #     根据传入的一组 isbn,到 Wish 表中计算出某个礼物的 Wish 心愿数量
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物,具体
    # 类代表礼物这个事物,它是抽象,不是具体的'一个'
    @classmethod
    def recent(cls):
        # 链式调用
        # 主题 Query
        # 子函数
        # 触发语句 first() all()
        recent_gift = Gift.query.filter_by(
            launched=False).order_by(
            desc(Gift.create_time)).distinct().limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
