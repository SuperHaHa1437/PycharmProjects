import os
import re

# package_path = input("请放入要打包的渠道文件夹：")
package_path = "/Users/superhaha/Desktop/huawei"
copyfile_src_path = package_path.replace(" ", "")  # 处理过后拷贝计费文件路径

next_dirs = ""  # 计费文件目录的下一层目录
for root, dirs, files in os.walk(copyfile_src_path):
    for name in dirs:
        next_dirs = os.path.join(root, name)
        print(next_dirs)

package_dirname = next_dirs.replace(" ", "")
package_dirname = package_dirname.split("/")[-1]
channel_list = list()  # channel list 表
mm_channel_value = ""  # 获取到mm渠道号


def getchannel():


    with open("/Users/superhaha/Desktop/huawei/华为/channel.txt", "r") as f:
        for line in f.readlines():
            linestr = line.strip()
            # print(linestr)
            linestrlist = re.split("\n|,", linestr)
            # linestrlist = linestr.split("\n")
            # linestrlist = linestr.split(",")
            # print(linestrlist)
            channel_list.append(linestrlist)
            # 遍历循环channel list
        for outresult in channel_list:
            for inresult in outresult:
                if package_dirname == inresult:
                    # print(outresult[0])
                    mm_channel_value = outresult[0]
                    print("联通渠道号：" + outresult[1])
                    print("电信渠道号:" + outresult[2])
                    print("包名:" + outresult[3])
                    print("versionCode:" + outresult[4])
                    print("versionName:" + outresult[5])
                    print("渠道号:" + outresult[6])
                    print("签名文件:" + outresult[7])
                    print("签名密码:" + outresult[8])
                    print("签名密码:" + outresult[9])
                    print("签名别名:" + outresult[10])
                    print("渠道名:" + outresult[11])
                    print("咪咕渠道号:" + outresult[12])
        if mm_channel_value == "":
            print("找不到匹配")
        else:
            print(mm_channel_value)

if __name__ == "__main__":
    getchannel()
