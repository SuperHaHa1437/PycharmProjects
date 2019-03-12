from flask import Flask

__author__ = '张'

app = Flask(__name__)
app.config.from_object('config')  # 载入配置文件,通过此种方式导入配置文件,配置参数必须为全大写字母


# 视图函数
@app.route('/hello')
def hello():
    return 'hello world'


# app.add_url_rule('/hello',view_func=hello)
# 入口
if __name__ == '__main__':
    # host = '0.0.0.0' 表示可外网访问
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
