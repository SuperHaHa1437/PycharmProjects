"""
Created by 张 on 2019/8/6 
"""
from flask import Blueprint

__author__ = '张'

# 实例化蓝图,以便视图函数可以插入到蓝图中
web = Blueprint('web', __name__)


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish