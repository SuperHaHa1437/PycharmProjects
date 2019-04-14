"""
Created by 张 on 2019/4/14 
"""
from flask import Blueprint
from . import web

__author__ = '张'

user = Blueprint('user',__name__)

# @web.route('/url')
def login():
    pass