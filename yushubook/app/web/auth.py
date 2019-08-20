# from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
# from app.libs.email import send_mail
# from app.models.base import db
# from app.models.user import User
from . import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    pass


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
