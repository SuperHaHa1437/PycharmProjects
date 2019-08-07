"""
Created by 张 on 2019/8/6 
"""
from flask import Flask

__author__ = '张'


def create_app():
    app = Flask(__name__)
    # 装载配置文件
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)
    return app


#  注册蓝图,以便注册在蓝图上的视图函数可以注册到应用 app 中
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)