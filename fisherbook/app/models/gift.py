"""
Created by 张 on 2019/6/30 
"""
from flask import current_app

from app.spider.yushu_book import YuShuBook

__author__ = '张'

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,desc
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

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
