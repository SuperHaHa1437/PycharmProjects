"""
Created by 张 on 2019/8/20 
"""
from sqlalchemy.orm import relationship

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func

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
