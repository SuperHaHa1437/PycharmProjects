"""
Created by 张 on 2019/4/9 
"""
from flask import Flask

__author__ = '张'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # 载入配置文件,通过此种方式导入配置文件,配置参数必须为全大写字母
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)