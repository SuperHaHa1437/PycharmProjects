import xml.dom.minidom
import codecs
import os
import shutil

# file_name = "/Users/superhaha/Desktop/huawei/AndroidManifest.xml"
# file_name = "/Users/superhaha/Desktop/apk/AndroidManifest.xml"
file_name = input("xml")
# file_name = "/Users/superhaha/Desktop/AndroidManifest.xml"
os.system("iconv -f gbk -t utf-8 " + file_name + "> " + os.getcwd() + "/AndroidManifest.xml")
shutil.copy(os.getcwd() + "/AndroidManifest.xml", "/Users/superhaha/Desktop")

dom = xml.dom.minidom.parse(file_name)
root = dom.documentElement
package = "com.ym"
metalist = root.getElementsByTagName("meta-data")
for item in metalist:
    meta_data_value = item.getAttribute("android:name")
    print(meta_data_value)
    if meta_data_value == "com.snowfish.appid":
        item.removeAttribute("android:name")
        item.removeAttribute("android:value")
    elif meta_data_value == "UMENG_CHANNEL":
        item.setAttribute("android:value", "了工程款")
    elif meta_data_value == "Countly_ChID":
        item.setAttribute("android:value", "安琪儿")
    elif meta_data_value == "EGAME_CHANNEL":
        item.setAttribute("android:value", "12345678")
    else:
        print("没有普通参数被替换")
#
root.setAttribute("package", "com.ym.xingppp")

servicelist = root.getElementsByTagName("action")
for item in servicelist:
    action_value = item.getAttribute("android:name")
    if action_value.endswith(".PUSH_ACTION"):
        item.setAttribute("android:name", package + ".PUSH_ACTION")
        print("替换PUSH_ACTION包名")
    else:
        print("没有信鸽service参数被更改")

providetlist = root.getElementsByTagName("provider")
for item in providetlist:
    provider_value = item.getAttribute("android:authorities")
    if provider_value.endswith(".AUTH_XGPUSH"):
        item.setAttribute("android:authorities", package + ".AUTH_XGPUSH")
        print("替换AUTH_XGPUSH包名")
    elif provider_value.endswith(".TPUSH_PROVIDER"):
        item.setAttribute("android:authorities", package + ".TPUSH_PROVIDER")
        print("替换TPUSH_PROVIDER包名")
    elif provider_value.endswith(".TENCENT.MID.V3"):
        item.setAttribute("android:authorities", package + ".TENCENT.MID.V3")
        print("替换TENCENT.MID.V3包名")
    else:
        print("没有信鸽provider参数被更改")

f = codecs.open(file_name, 'w', 'utf-8')
dom.writexml(f, indent='', addindent='\t', newl='', encoding='UTF-8')


# if __name__ == "__main__":
