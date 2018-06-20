import os
import time

num = input("微信：")
choice = input("5-只退出 6-只登录 功能：")


def login():
    if num == "1":
        os.system("adb shell input text  15519586588")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  leyouyou123")
        os.system("adb shell input tap 500 1100")
    elif num == "2":
        os.system("adb shell input text  17712863270")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  ym12345678")
        os.system("adb shell input tap 500 1100")
    elif num == "3":
        os.system("adb shell input text  13519753806")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  ym12345678")
        os.system("adb shell input tap 500 1100")
    elif num == "4":
        os.system("adb shell input text  17373587714")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  123456789Cz")
        os.system("adb shell input tap 500 1100")
    elif num == "5":
        os.system("adb shell input text  15021323174")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  youmeng2018")
        os.system("adb shell input tap 500 1100")
    elif num == "6":
        os.system("adb shell input text  19919921465")
        os.system("adb shell input tap 500 1100")
        time.sleep(1)
        os.system("adb shell input text  ym12345678")
        os.system("adb shell input tap 500 1100")


def exit():
    os.system("adb shell input tap 950 1830")  # 我
    os.system("adb shell input tap 500 1300")  # 设置
    os.system("adb shell input swipe 650 1600 650 1000")  # 划至顶部
    os.system("adb shell input tap 500 1800")  # 退出
    os.system("adb shell input tap 500 1700")  # 退出登陆
    os.system("adb shell input tap 800 1111")  # 退出登陆


if __name__ == "__main__":
    if choice == "5":
        print("只退出")
        exit()
    elif choice == "6":
        print("只登录")
        os.system("adb shell input tap 780 1850")  # 更多
        os.system("adb shell input tap 500 1440")  # 登陆其他账号
        login()
    else:
        print("退出并登录")
        exit()
        time.sleep(9)
        print("睡眠结束")
        os.system("adb shell input tap 780 1850")  # 更多
        os.system("adb shell input tap 500 1440")  # 登陆其他账号
        login()
