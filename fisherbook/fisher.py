
from app import create_app

__author__ = '张'

app = create_app()


if __name__ == '__main__':
    # host = '0.0.0.0' 表示可外网访问
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
