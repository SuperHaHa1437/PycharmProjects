# -*- coding:UTF-8 -*-
import os
import re

# package_path = input("请放入要打包的渠道文件夹：")
# package_path = "/Users/superhaha/Desktop/huawei"
# copyfile_src_path = package_path.replace(" ", "")  # 处理过后拷贝计费文件路径
#
# next_dirs = ""  # 计费文件目录的下一层目录
# for root, dirs, files in os.walk(copyfile_src_path):
#     for name in dirs:
#         next_dirs = os.path.join(root, name)
#         print(next_dirs)

# package_dirname = next_dirs.replace(" ", "")
package_dirname = "华为"
# package_dirname = package_dirname.split("/")[-1]
channel_list = list()  # channel list 表
# mm_channel_value = ""  # 获取到mm渠道号
mm_channel_value = ""  # mm渠道号
egame_channel_value = ""  # 电信渠道号
package_name = ""  # 包名
versioncode_value = ""  # versioncode
versionname_value = ""  # versionname
channel_num = ""  # 渠道号
sign_file = ""  # 签名文件
sign_pwd = ""  # 签名密码
sign_alias = ""  # 签名文件别名
channel_name = ""  # 渠道名
jinshan_channel = ""  # 金山渠道号

def getchannel():
    with open("/Users/superhaha/Desktop/normal/channel.txt", "r") as f:
        for line in f.readlines():
            linestr = line.strip()
            # print(linestr)
            # print(package_dirname)
            linestrlist = re.split("\n|,", linestr)
            channel_list.append(linestrlist)
            # 遍历循环channel list
        for outresult in channel_list:
            for inresult in outresult:
                if package_dirname == inresult:
                    # print(outresult[0])
                    global mm_channel_value, egame_channel_value, package_name, versioncode_value, versionname_value, channel_num, sign_file, sign_pwd, sign_alias, channel_name, jinshan_channel
                    mm_channel_value = outresult[0]
                    egame_channel_value = outresult[2]
                    package_name = outresult[3]
                    versioncode_value = outresult[4]
                    versionname_value = outresult[5]
                    channel_num = outresult[6]
                    sign_file = outresult[7]
                    sign_pwd = outresult[8]
                    sign_alias = outresult[10]
                    channel_name = outresult[11]
                    jinshan_channel = outresult[12]

        if package_dirname == "":
            print("找不到渠道匹配")
        else:
            print("MM渠道号:" + mm_channel_value)
            print("电信渠道号:" + egame_channel_value)
            print("包名:" + package_name)
            print("versionCode:" + versioncode_value)
            print("versionName:" + versionname_value)
            print("渠道号:" + channel_num)
            print("签名文件:" + sign_file)
            print("签名密码:" + sign_pwd)
            print("签名别名:" + sign_alias)
            print("渠道名:" + channel_name)
            print("金山渠道号:" + jinshan_channel)

if __name__ == "__main__":
    getchannel()
