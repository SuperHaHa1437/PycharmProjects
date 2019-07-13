"""
Created by 张 on 2019/1/18
配置文件
"""
__author__ = '张'

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:password@localhost:3306/fisher'
SECRET_KEY = 'E92fj5J9'

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '565393394@qq.com'
MAIL_PASSWORD = 'pmwqxdholzgkbecc'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书 <hello@yushu.im>'
