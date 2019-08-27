from flask import current_app, flash, redirect, url_for, render_template

# from app.libs.enums import PendingStatus
# from app.models.base import db
# from app.models.drift import Drift
# from app.models.gift import Gift
# from app.view_models.trade import MyTrades
from app.models.base import db
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    """
    1.获取用户 id
    2.查询此 id 下所有符合查询条件的Gift模型
    3.遍历符合条件的Gift 模型,取出其 isbn 组成 isbn_list
    4.查询isbn_list下每一个 isbn 对应的心愿数,组成wish_count_list
    5.通过 viewmodel解析获取能渲染到页面的数据,拿到isbn 匹配书籍详情数据,每一本图书对应的心愿数.
    :return:
    """
    uid = current_user.id
    gift_of_mine = Gift.get_user_gift(uid)
    isbn_list = [gift.isbn for gift in gift_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyGifts(gift_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """
    赠送书籍视图函数
    current_user 即为 User 模型的实例,通过.id 拿到当前用户的 id号
    原本用户 id 存储在 cookie 中,只是一个 id 属性,但通过 User模型下 get_user 函数
    此函数内部实现将 id 转换成对象模型
    :param isbn:
    """
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单,请不要重复添加')

    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    pass
