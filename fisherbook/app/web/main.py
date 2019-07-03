from . import web


@web.route('/')
def index():
    return 'index page'


@web.route('/personal')
def personal_center():
    pass
