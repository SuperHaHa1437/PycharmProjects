"""
Created by 张 on 2019/6/30 
"""
from flask import current_app

__author__ = '张'

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    def recent(self):
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gift
