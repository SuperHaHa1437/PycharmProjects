# -*- coding:UTF-8 -*-
import os
import re
import sys
import xml.dom.minidom
import shutil
import zipfile
import codecs

# apk_file_name = input("请放入母包:")  # 反编译的apk文件
# channel_path = input("请放入渠道channel.txt:")  # 渠道channel文件路径
# package_path = input("请放入要打包的渠道文件夹:")  # 计费文件路径
# gameversion = input("请确认游戏版本 1-封测 2-发行:")
apk_file_name = "/Users/superhaha/Desktop/apk/templateisdk-ym_isdk-release.apk "  # 反编译的apk文件
channel_path = "/Users/superhaha/Desktop/normal/channel.txt"  # 渠道channel文件路径
package_path = "/Users/superhaha/Desktop/normal"  # 计费文件路径
gameversion = "1"
apk_path = os.path.dirname(apk_file_name)  # 反编译apk文件目录名称
apk_dirname = os.path.splitext(os.path.basename(apk_file_name))[0]  # 获得反编译apk文件目录名称
apk_extension = os.path.splitext(os.path.basename(apk_file_name))[1]  # 获得apk文件后缀
channel_txt = channel_path.replace(" ", "")  # 格式化channel.txt路径,去除空格
copyfile_src_path = package_path.replace(" ", "")  # 格式化拷贝计费文件路径,去除空格

next_dirs_list = list()  # 获取到多个渠道目录
for root, dirs, files in os.walk(copyfile_src_path):
    for name in dirs:
        next_dirs = os.path.join(root, name)  # next_dirs渠道计费文件目录的下一层目录,即第二层索引目录
        next_dirs_list.append(name)
        print(next_dirs_list)

channel_list = list()  # channel list 表
copyfile_dest_path = os.path.join(os.getcwd(), apk_dirname)  # 拷贝计费文件目标目录
log_file_path = os.path.join(os.getcwd(), "log")  # 解压联通计费文件目录

file_list = os.listdir(next_dirs)  # 计费文件目录文件列表

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

print("os.getwcd:" + os.getcwd())
print("apkpath:" + apk_path)
print("apk_dirname:" + apk_dirname)
print("apk_extension:" + apk_extension)
print("copyfile_src_path:" + copyfile_src_path)
print("copyfile_dest_path:" + copyfile_dest_path)
print("log_file_path:" + log_file_path)
print("gameversion:" + gameversion)
print("next_dirs:" + next_dirs)


def decompilation(apk_file_name):
    print("执行反编译")
    for root, dirs, files in os.walk(apk_path):
        for file in files:
            apk_file_name = os.path.join(root, file)
            if apk_file_name.endswith(".apk"):
                apktool_command = "apktool d -f " + apk_file_name  # 反编译apk并强制删除之前的文件夹
                os.system(apktool_command)


def getchannel():
    with open(channel_txt, "r") as f:
        for line in f.readlines():
            linestr = line.strip()
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


def jieyafile():
    for first_file_name in file_list:  # 第一层压缩文件
        if os.path.splitext(first_file_name)[1] == ".zip":
            file_zip = zipfile.ZipFile(next_dirs + "/" + first_file_name, "r")

            for second_file_name in file_zip.namelist():  # 第二层压缩文件由第一层解压出的文件
                file_zip.extract(second_file_name, log_file_path)

                if os.path.splitext(second_file_name)[1] == ".zip":
                    # second_file_zip = zipfile.ZipFile(log_file_path + "/" + second_file_name, "r")
                    file_zip = zipfile.ZipFile(log_file_path + "/" + second_file_name, "r")

                    # for third_file_name in second_file_zip.namelist():#由第二层压缩文件解压出的第三层文件
                    #     second_file_zip.extract(third_file_name, log_file_path)

                    for third_file_name in file_zip.namelist():  # 由第二层压缩文件解压出的第三层文件
                        file_zip.extract(third_file_name, log_file_path)
                        # print(third_file_name)

                        if os.path.splitext(third_file_name)[0] == "Multimode_UniPay_payinfo":
                            file_zip = zipfile.ZipFile(log_file_path + "/" + "Multimode_UniPay_payinfo.jar", "r")
                            for final_file_name in file_zip.namelist():
                                file_zip.extract(final_file_name, log_file_path)
                            break

                        file_zip.close()


def copyfiles():
    print("复制mmiap.xml")
    # try:
    shutil.copy(next_dirs + "/mmiap.xml", copyfile_dest_path + "/unknown")
    print("复制联通计费文件")
    shutil.copy(log_file_path + "/assets/UnicomConsume/UnicomConsume.uwc", copyfile_dest_path + "/assets/UnicomConsume")
    shutil.rmtree(log_file_path)


def modifyversion():
    with open(copyfile_dest_path + "/apktool.yml", 'r+')as f:
        file_data = ''
        for line in f.readlines():
            if line.find('versionCode') == 0 or line.find('versionCode') == 2:
                line = "  versionCode: '" + versioncode_value + "'" + '\n'
            if line.find('versionName') == 0 or line.find('versionName') == 2:
                line = "  versionName: '" + versionname_value + "'"
            file_data += line
        print(file_data)
    with open(copyfile_dest_path + "/apktool.yml", 'r+')as f:
        f.writelines(file_data)


def modifymanifest():
    dom = xml.dom.minidom.parse(copyfile_dest_path + "/AndroidManifest.xml")
    root = dom.documentElement

    metalist = root.getElementsByTagName("meta-data")
    for item in metalist:
        meta_data_value = item.getAttribute("android:name")
    #     # print(meta_data_value)
        if meta_data_value == "UMENG_CHANNEL":
            item.setAttribute("android:value", channel_name)
            print("修改友盟参数")
        elif meta_data_value == "com.snowfish.appid" and channel_name == "华为":
            # item.removeAttribute("android:name")
            # item.removeAttribute("android:value")
            item.setAttribute("android:name", "")
            item.setAttribute("android:value", "")
            print("删除易接参数")
        elif meta_data_value == "channel_name":
            item.setAttribute("android:value", channel_name)
            print("修改统计参数")
        elif meta_data_value == "jinshan_chId":
            item.setAttribute("android:value", jinshan_channel)
            print("修改金山渠道号")
        elif meta_data_value == "EGAME_CHANNEL":
            item.setAttribute("android:value", egame_channel_value)
            print("修改电信渠道号")
        else:
            pass
    #         # print("没有普通参数被替换")

    root.setAttribute("package", package_name)

    servicelist = root.getElementsByTagName("action")
    for item in servicelist:
        action_value = item.getAttribute("android:name")
        if action_value.endswith(".PUSH_ACTION"):
            item.setAttribute("android:name", package_name + ".PUSH_ACTION")
            print("替换PUSH_ACTION包名")
        else:
            pass
            # print("没有信鸽service包名参数被更改")

    providetlist = root.getElementsByTagName("provider")
    for item in providetlist:
        provider_value = item.getAttribute("android:authorities")
        if provider_value.endswith(".AUTH_XGPUSH"):
            item.setAttribute("android:authorities", package_name + ".AUTH_XGPUSH")
            print("替换AUTH_XGPUSH包名")
        elif provider_value.endswith(".TPUSH_PROVIDER"):
            item.setAttribute("android:authorities", package_name + ".TPUSH_PROVIDER")
            print("替换TPUSH_PROVIDER包名")
        elif provider_value.endswith(".TENCENT.MID.V3"):
            item.setAttribute("android:authorities", package_name + ".TENCENT.MID.V3")
            print("替换TENCENT.MID.V3包名")
        else:
            pass
            # print("没有信鸽provider包名参数被更改")

    f = codecs.open(copyfile_dest_path + "/AndroidManifest.xml", 'w', 'UTF-8')
    dom.writexml(f, indent='', addindent='', newl='', encoding='UTF-8')


def move_apk():
    # 删除已存在的渠道包
    for dest_apk in os.listdir(copyfile_src_path):
        if dest_apk.endswith(".apk"):
            os.remove(copyfile_src_path + "/" + dest_apk)
    # 移动生成渠道包
    for apk_file in os.listdir(os.getcwd()):
        if apk_file.endswith(".apk"):
            shutil.move(apk_file, copyfile_src_path)
    # 删除反编译文件夹
    shutil.rmtree(copyfile_dest_path)


if __name__ == "__main__":
    if gameversion == "2":
        print("执行发行打包")
        decompilation(apk_file_name)
        # os.system("iconv -f gbk -t utf-8 " + copyfile_dest_path + "/AndroidManifest.xml" + "> " + os.getcwd() + "/AndroidManifest.xml")
        # shutil.copy(os.getcwd() + "/AndroidManifest.xml",copyfile_dest_path)
        for next_dir_name in next_dirs_list:
            package_dirname = next_dir_name  # package_dirname 计费文件目录名
            getchannel()
            jieyafile()
            copyfiles()
            modifyversion()
            modifymanifest()
            os.system("apktool b " + copyfile_dest_path)
            apk_sign_command = "jarsigner -keystore " + copyfile_src_path + "/" + sign_file + " -signedjar " + apk_dirname + "_" + package_dirname + apk_extension + copyfile_dest_path + "/dist/" + apk_dirname + apk_extension + sign_alias + " -storepass 111111"
            os.system(apk_sign_command)
        move_apk()
    else:
        print("执行封测打包")
        decompilation(apk_file_name)
        for next_dir_name in next_dirs_list:
            package_dirname = next_dir_name  # package_dirname 计费文件目录名
            getchannel()
            # modifyversion()
            modifymanifest()
            os.system("apktool b " + copyfile_dest_path)
            apk_sign_command = "jarsigner -keystore " + copyfile_src_path + "/" + sign_file + " -signedjar " + apk_dirname + "_" + package_dirname + apk_extension + copyfile_dest_path + "/dist/" + apk_dirname + apk_extension + sign_alias + " -storepass 111111"
            os.system(apk_sign_command)
        move_apk()
