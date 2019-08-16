"""
Created by 张 on 2019/8/6 
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

__author__ = '张'


# 验证 web下 book 中 search 视图函数的两个参数
class SearchForm(Form):
    # 搜索的参数,isbn或者关键字
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    # 搜索结果的页数,默认值为 1,最小值为 1,最大值为 99
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
