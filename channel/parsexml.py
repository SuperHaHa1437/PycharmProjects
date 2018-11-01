# -*- coding:UTF-8 -*-
from xml.etree import ElementTree
import os
import sys

# apk_zipalign_command = "zipalign -v 4 " + os.getcwd() + "/" + apk_dirname + "_" + package_dirname + apk_extension + " " + apk_dirname + "_" + package_dirname + "_align" + apk_extension
# os.system(apk_zipalign_command)

if __name__ == "__main__":
    xmlfilepath = os.path.abspath("/Users/superhaha/Desktop/mmiap.xml")
    print("xml文件路径：", xmlfilepath)

    # 得到文档对象
    domobj = ElementTree.parse(xmlfilepath)
    # print("xmldom.parse:", type(domobj))

    subElementObj = domobj.find("./channel")
    print(subElementObj)
    subElementObj.text = "1234567890"
    domobj.write("/Users/superhaha/Desktop/mmiap.xml", xml_declaration=True, encoding="UTF-8", method="xml")
