"""
Created by 张 on 2019/8/20 
"""
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func

from app.spider.yushu_book import YuShuBook

__author__ = '张'


# 心愿模型类
class Wish(Base):
    id = Column(Integer, primary_key=True)
    # user 需要关联 User 模型
    user = relationship('User')
    # 拿到用户的唯一标识,也是 User模型类下的 id
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
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
