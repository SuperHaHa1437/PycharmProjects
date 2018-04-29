import os
import re
import sys
import xml.dom.minidom
import shutil
import zipfile

# apk_file_name = input("请放入母包:")  # 反编译的apk文件
# channel_path = input("请放入渠道channel.txt")  # 渠道channel文件路径
# package_path = input("请放入要打包的渠道文件夹:")  # 计费文件路径
apk_file_name = "/Users/superhaha/Desktop/apk/templateisdk-ym_isdk-release.apk "  # 反编译的apk文件
channel_path = "/Users/superhaha/Desktop/huawei/华为/channel.txt"  # 渠道channel文件路径
package_path = "/Users/superhaha/Desktop/huawei"  # 计费文件路径
apk_path = os.path.dirname(apk_file_name)
apk_dirname = os.path.splitext(os.path.basename(apk_file_name))[0]  # 获得反编译apk文件目录名称
channel_txt = channel_path.replace(" ", "")
# package_dirname = package_path.replace(" ", "") and package_path.split("/")[-1]
copyfile_src_path = package_path.replace(" ", "")  # 处理过后拷贝计费文件路径

next_dirs = ""  # 计费文件目录的下一层目录
for root, dirs, files in os.walk(copyfile_src_path):
    for name in dirs:
        next_dirs = os.path.join(root, name)
        print(next_dirs)

package_dirname = next_dirs.replace(" ", "")
package_dirname = package_dirname.split("/")[-1]
channel_list = list()  # channel list 表
copyfile_dest_path = os.path.join(os.getcwd(), apk_dirname)  # 拷贝计费文件目标目录
log_file_path = os.path.join(os.getcwd(), "log")  # 解压联通计费文件目录

file_list = os.listdir(next_dirs)  # 计费文件目录文件列表

mm_channel_value = ""  # 获取到mm渠道号
egame_channel_value = ""  # 获取到电信渠道号
package_name = ""  # 获取到包名
versioncode_value = ""  # 获取到versioncode
versionname_value = ""  # 获取到versionname
channel_num = ""  # 获取到渠道号
sign_file = ""  # 签名文件
sign_pwd = ""  # 签名密码
sign_alias = ""  # 签名文件别名
channel_name = ""  # 获取到渠道名


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
            # print(linestr)
            # print(package_dirname)
            linestrlist = re.split("\n|,", linestr)
            channel_list.append(linestrlist)
            # 遍历循环channel list
        for outresult in channel_list:
            for inresult in outresult:
                if package_dirname == inresult:
                    # print(outresult[0])
                    global mm_channel_value, egame_channel_value, package_name, versioncode_value, versionname_value, channel_num, sign_file, sign_pwd, sign_alias, channel_name
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

        if package_dirname == "":
            print("找不到匹配")
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
                line = "  versionName: " + versionname_value
            file_data += line
        print(file_data)
    with open(copyfile_dest_path + "/apktool.yml", 'r+')as f:
        f.writelines(file_data)


def modifymanifest():
    dom = xml.dom.minidom.parse(copyfile_dest_path + "/AndroidManifest.xml")
    root = dom.documentElement

    itemlist = root.getElementsByTagName("meta-data")
    for item in itemlist:
        meta_data_value = item.getAttribute("android:name")
        print(meta_data_value)
        if meta_data_value == "UMENG_CHANNEL":
            item.setAttribute("android:value", channel_name)
        if meta_data_value == "Countly_ChID":
            item.setAttribute("android:value", channel_name)
        if meta_data_value == "EGAME_CHANNEL":
            item.setAttribute("android:value", egame_channel_value)
            break
    root.setAttribute("package", package_name)
    f = open(copyfile_dest_path + "/AndroidManifest.xml", 'w')
    dom.writexml(f, indent='', addindent='', newl='', encoding='UTF-8')
    pass


if __name__ == "__main__":
    decompilation(apk_file_name)
    getchannel()
    jieyafile()
    copyfiles()
    modifyversion()
    modifymanifest()
    os.system("apktool b "+copyfile_dest_path)
    os.system("jarsigner -verbose -keystore /Users/superhaha/Desktop/alias-111111.keystore -signedjar template_sign.apk "+copyfile_dest_path+"/dist"+"/templateisdk-ym_isdk-release.apk "+"alias")