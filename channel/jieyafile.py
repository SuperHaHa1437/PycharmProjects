import zipfile
import os

src_file_path = "/Users/superhaha/Desktop/huawei"
log_file_path = os.path.join(src_file_path, "log")

for root,dirs,files in os.walk(src_file_path):
    for name in dirs:
        next_dirs = os.path.join(root,name)
        print(next_dirs)

file_list = os.listdir(next_dirs)

for first_file_name in file_list:#第一层压缩文件
    if os.path.splitext(first_file_name)[1] == '.zip':
        file_zip = zipfile.ZipFile(next_dirs + '/' + first_file_name, 'r')

        for second_file_name in file_zip.namelist():#第二层压缩文件由第一层解压出的文件
            file_zip.extract(second_file_name, log_file_path)

            if os.path.splitext(second_file_name)[1] == '.zip':
                # second_file_zip = zipfile.ZipFile(log_file_path + '/' + second_file_name, 'r')
                file_zip = zipfile.ZipFile(log_file_path + '/' + second_file_name, 'r')

                # for third_file_name in second_file_zip.namelist():#由第二层压缩文件解压出的第三层文件
                #     second_file_zip.extract(third_file_name, log_file_path)

                for third_file_name in file_zip.namelist():#由第二层压缩文件解压出的第三层文件
                    file_zip.extract(third_file_name, log_file_path)
                    print(third_file_name)

                    if os.path.splitext(third_file_name)[0] == 'Multimode_UniPay_payinfo':
                        file_zip = zipfile.ZipFile(log_file_path+'/'+'Multimode_UniPay_payinfo.jar','r')
                        for final_file_name in file_zip.namelist():
                            file_zip.extract(final_file_name,log_file_path)
                        break

                    file_zip.close()

