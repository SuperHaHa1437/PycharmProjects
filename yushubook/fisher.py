"""
Created by 张 on 2019/8/5 
"""
from flask import Flask

from app import create_app

__author__ = '张'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
