"""
Created by 张 on 2019/8/6 
"""
from flask import Flask

from app.models.book import db

__author__ = '张'


def create_app():
    """

    :return: 返回 flask 核心对象
    """
    app = Flask(__name__)
    # 装载配置文件
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    # 在 flask 核心对象中注册蓝图
    register_blueprint(app)

    db.init_app(app)
    # create_all 就是可以将业务模型创建到数据库中
    db.create_all(app=app)
    return app


#  注册蓝图,以便注册在蓝图上的视图函数可以注册到应用 app 中
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
