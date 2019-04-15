# -*- coding:UTF-8 -*-
import os
import time
import mysql.connector


class WeChatLogin():
    num = input('微信账户选择：')
    choice = input('5:只退出 6:只登录 模式选择：')

    conn = mysql.connector.connect(user='root', password='password', database='wechat_database')
    cursor = conn.cursor()
    cursor.execute('select * from account_tables')
    account_list = cursor.fetchall()


    # 装饰器,用作登陆时点击更多并登陆其他账号的操作
    def more_login_decorator(func):
        def wrapper(*args):
            print('正在登陆新账户')
            os.system('adb shell input tap 780 1850')  # 更多
            os.system('adb shell input tap 500 1440')  # 登陆其他账号
            func(*args)

        return wrapper

    @more_login_decorator
    def login(self):
        os.system('adb shell input text ' + WeChatLogin.account_list[int(WeChatLogin.num)][0])
        os.system('adb shell input tap 500 1100')
        time.sleep(1)
        os.system('adb shell input text ' + WeChatLogin.account_list[int(WeChatLogin.num)][1])
        os.system('adb shell input tap 500 1100')
        print('登陆成功')

    def exit_wechat(self):
        os.system('adb shell input tap 950 1830')  # 我
        os.system('adb shell input tap 400 1600')  # 设置
        os.system('adb shell input swipe 650 1600 650 1000')  # 划至顶部
        os.system('adb shell input tap 500 1800')  # 退出
        os.system('adb shell input tap 500 1700')  # 退出登陆
        os.system('adb shell input tap 800 1111')  # 退出登陆
        print('已退出当前账户')


wechat = WeChatLogin()
if WeChatLogin.choice == '5':
    wechat.exit_wechat()

elif WeChatLogin.choice == '6':
    wechat.login()

else:
    print('退出并登陆新账户')
    wechat.exit_wechat()
    time.sleep(9)
    wechat.login()
