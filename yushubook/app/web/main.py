from flask import render_template

# from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web


@web.route('/')
def index():
    return 'index'


@web.route('/personal')
def personal_center():
    pass
