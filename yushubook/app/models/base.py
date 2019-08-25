"""
Created by 张 on 2019/8/20 
"""
from contextlib import contextmanager
from datetime import datetime

__author__ = '张'

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, Integer, SmallInteger

'''
继承第三方类库SQLAlchemy,以自定义需要的方法
'''


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        """
        如果其中一个在执行过程中失败了，那么另一个也不能提交，这用到了数据库的事务
        """
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        """
        重写 filter_by
        由于我们的删除操作都是逻辑删除 , 所以在查询的时候应该默认查询 status=1 的记录 (即未删除的记录),
         但是如果在每一个 filter_by 里都这么写，就太麻烦了，
         我们的思路是重写默认的 filter_by 函数，加上 status=1 的限制条件.
        :param kwargs:
        :return:
        """
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    # 状态
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        """
        如果说 atts_dict 字典中的某一个 key 和模型中的某一个属性相同
        就把字典的 key 所对应的值赋给模型的相关属性
        :param attrs_dict: 字典类型参数
        """
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        """
        create_time 本是 int 类型，要进行 strftime 格式化操作需要转化成 string 类型
        :return:
        """
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
