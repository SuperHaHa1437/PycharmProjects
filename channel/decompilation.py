import os

def decompilation(apk_file_name):
    print("执行反编译")
    for root, dirs, files in os.walk(apk_path):
        for file in files:
            apk_file_name = os.path.join(root, file)
            if apk_file_name.endswith(".apk"):
                apktool_command = "apktool d -f " + apk_file_name  # 反编译apk并强制删除之前的文件夹
                os.system(apktool_command)