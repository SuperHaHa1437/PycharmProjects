"""
Created by 张 on 2019/7/13 
"""
from flask import current_app, render_template

__author__ = '张'

from app import mail
from flask_mail import Message


def send_mail(to, subject, template, **kwargs):
    # msg = Message('鱼书测试邮件', sender='565393394@qq.com', body='Test',
    #               recipients=['565393394@qq.com'])
    msg = Message('[鱼书]' + ' ' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
