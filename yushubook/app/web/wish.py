from flask import current_app, flash, redirect, url_for, render_template

# from app.libs.email import send_mail
# from app.models.base import db
# from app.models.gift import Gift
# from app.models.wish import Wish
# from app.view_models.trade import MyTrades
from app.models.base import db
from app.models.wish import Wish
from . import web
from flask_login import login_required, current_user


@web.route('/my/wish')
@login_required
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
            flash('书籍加入心愿清单成功')
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单,请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
