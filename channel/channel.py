import os
import re

package_path = input("请放入要打包的渠道文件夹：")
package_dirname = package_path.replace(" ", "")
package_dirname = package_dirname.split("/")[-1]
mm_channel_value = ""  # 获取到mm渠道号
channel_list = list()  # channel list 表


def getchannel():
    with open("/Users/superhaha/Desktop/apk/channel.txt", "r") as f:
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

        if mm_channel_value == "":
            print("找不到匹配")
        else:
            print(mm_channel_value)


if __name__ == "__main__":
    getchannel()
