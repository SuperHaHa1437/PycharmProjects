# -*- coding:UTF-8 -*-
import re

file = '/Users/superhaha/Desktop/huawei/apktool.yml'
new_versionCode = "  versionCode: '" + '4' + "'"
new_versionName = "  versionName: '" + '1.3' + "'"

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
