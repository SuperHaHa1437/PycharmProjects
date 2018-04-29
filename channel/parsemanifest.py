from xml.etree.ElementTree import ElementTree, Element
import xml.dom.minidom
import xml.etree.ElementTree as ET

file_name = "/Users/superhaha/Desktop/huawei/AndroidManifest.xml"

dom = xml.dom.minidom.parse(file_name)
root = dom.documentElement

itemlist = root.getElementsByTagName("meta-data")
for item in itemlist:
    meta_data_value = item.getAttribute("android:name")
    print(meta_data_value)
    if meta_data_value == "UMENG_CHANNEL":
        item.setAttribute("android:value", "小康")
    if meta_data_value == "Countly_ChID":
        item.setAttribute("android:value", "顺德区")
    if meta_data_value == "EGAME_CHANNEL":
        item.setAttribute("android:value", "12345678")
        break
root.setAttribute("package","com.ym.xingppp")
f = open(file_name, 'w')
dom.writexml(f, indent='', addindent='', newl='', encoding='UTF-8')


# if __name__ == "__main__":
