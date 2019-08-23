# from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
# from app.libs.email import send_mail
# from app.models.base import db
# from app.models.user import User
from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        user = User()
        # 动态赋值: 将网页表单获取到的值,与模型中属性查询对应,有对应的就将其赋值给该属性
        user.set_attrs(form.data)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    """
    登陆页面
    :return:
    """
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            # next 是登陆后的页面url地址有 next 参数,表明登陆后要跳转的页面地址
            next = request.args.get('next')
            # 避免重定向攻击
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账户不存在或者密码错误')
    return render_template('auth/login.html', form=form)


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
