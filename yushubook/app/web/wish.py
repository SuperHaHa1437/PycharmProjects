from flask import current_app, flash, redirect, url_for, render_template

# from app.libs.email import send_mail
# from app.models.base import db
# from app.models.gift import Gift
# from app.models.wish import Wish
# from app.view_models.trade import MyTrades
from . import web
from flask_login import login_required, current_user


@web.route('/my/wish')
@login_required
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
