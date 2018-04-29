import re

file = '/Users/superhaha/Desktop/huawei/华为/apktool.yml'
new_versionCode = "  versionCode: '" + '100' + "'"
new_versionName = "  versionName:" + " 100.112.112"

with open(file, 'r+')as f:
    file_data = ''
    for line in f.readlines():
        if line.find('versionCode') == 0 or line.find('versionCode') == 2:
            line = new_versionCode + '\n'
        if line.find('versionName') == 0 or line.find('versionName') == 2:
            line = new_versionName
        print(line.find('versionCode'))
        file_data += line
    print(file_data)
with open(file, 'r+')as f:
    f.writelines(file_data)
