"""
Created by 张 on 2019/8/20 
"""
from werkzeug.security import generate_password_hash

from app.models.base import db, Base
from sqlalchemy import Column, Integer, String, Boolean, Float

__author__ = '张'


# 用户模型类
class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        """
        password属性读取
        :return:
        """
        return self._password

    @password.setter
    def password(self, raw):
        """
        password属性写入
        :param raw: 原始password
        """
        self._password = generate_password_hash(raw)
