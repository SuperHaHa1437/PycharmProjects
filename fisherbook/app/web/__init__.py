"""
Created by 张 on 2019/4/21 
"""
from flask import Blueprint

__author__ = '张'

web = Blueprint('web', __name__)

from app.web import book
from app.web import user