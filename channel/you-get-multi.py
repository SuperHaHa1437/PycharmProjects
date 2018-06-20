import os
import time

download_url = input("输入下载链接:")
download_path = input("输入下载路径:")

if __name__ == "__main__":
    print("下载链接信息")
    os.system("you-get -i "+download_url)
    time.sleep(5)
    print("开始下载")
    os.system("you-get -o "+download_path+download_url)