"""
Created by 张 on 2019/8/20 
"""
__author__ = '张'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 状态
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        """
        如果说 atts_dict 字典中的某一个 key 和模型中的某一个属性相同
        就把字典的 key 所对应的值赋给模型的相关属性
        :param attrs_dict: 字典类型参数
        """
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
