"""
Created by 张 on 2019/8/21 
"""
from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError, EqualTo

from app.models.user import User

__author__ = '张'


# 注册表单参数校验
class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入你的密码'), Length(6, 32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符,最多10个字符')])

    def validate_email(self, field):
        """
        自定义校验器,校验邮箱,函数名 validate_email 会自动识别对 email 校验
        first()无论查询多少条都只返回一条
        :param field:客户端传入的参数
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')


# 登陆表单校验参数
class LoginForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空,请输入你的密码'), Length(6, 32)])
