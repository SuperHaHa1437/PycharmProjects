# -*- coding:UTF-8 -*-
import os
import time

download_url = input("输入下载链接:")

if __name__ == "__main__":
    print("下载链接信息")
    os.system("you-get -i "+download_url)
    time.sleep(5)
    print("开始下载")
    os.system("you-get -o /Users/superhaha/Downloads "+download_url)