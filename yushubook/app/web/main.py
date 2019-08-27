from flask import render_template

# from app.models.gift import Gift
from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web


@web.route('/')
def index():
    """
    最近的赠送礼物将显示在主页
    :return:
    """
    recent_gifts = Gift.recent_gift()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass
