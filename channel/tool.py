import os, re, sys, shutil

filename = input('请放入母包:')  # 反编译的apk文件
# channel_path = input('请放入渠道channel.txt')  # 渠道channel文件路径
package_path = input('请放入要打包的渠道文件夹:')  # 计费文件路径
apk_path = os.path.dirname(filename)
apk_dirname = os.path.splitext(os.path.basename(filename))[0]  # 获得反编译apk文件目录名称
# channel_txt = channel_path.replace(' ', '')
package_dirname = package_path.replace(' ', '') and package_path.split('/')[-1]
copyfile_src_path = package_path.replace(' ', '')  # 拷贝计费文件路径
copyfile_dest_path = os.path.join(os.getcwd(), apk_dirname)

mm_channel_value = ''  # 获取到mm渠道号
channel_list = list()  # channel list 表


def decompilation(filename):
    print('执行反编译')
    for root, dirs, files in os.walk(apk_path):
        for file in files:
            filename = os.path.join(root, file)
            if filename.endswith('.apk'):
                apktool_command = 'apktool d -f ' + filename  # 反编译apk并强制删除之前的文件夹
                os.system(apktool_command)


def getchannel():
    # with open('/Users/superhaha/Desktop/apk/channel.txt', 'r') as f:
    with open(channel_txt, 'r') as f:
        for line in f.readlines():
            linestr = line.strip()
            # print(linestr)
            linestrlist = re.split('\n|,', linestr)
            channel_list.append(linestrlist)
            # 遍历循环channel list
        for outresult in channel_list:
            for inresult in outresult:
                if package_dirname == inresult:
                    # print(outresult[0])
                    mm_channel_value = outresult[0]

        if mm_channel_value == '':
            print('找不到匹配')
        else:
            print(mm_channel_value)


def copymmiap():
    print('复制mmiap.xml')
    try:
        shutil.copy(copyfile_src_path + '/mmiap.xml', copyfile_dest_path + '/unknown')
    


if __name__ == '__main__':
    decompilation(filename)
    copymmiap()
