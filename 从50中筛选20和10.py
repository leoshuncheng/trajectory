import shutil
import os,re,sys,scipy.stats as st

RootPath = "D:\\trajectory_last\\服务器上拷过来的\\Geolife20afterMD" #要先把50的文件拷贝进去，然后修改路径名

def file_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return files

print(file_names(RootPath))

file_list = file_names(RootPath)
for file in file_list:
    # 将文件读取到内存中
    with open(RootPath+ "\\" + file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 写的方式打开文件
    with open(RootPath+ "\\" + file, "w", encoding="utf-8") as f_w:
        count = 0
        templine = ''
        for line in lines:
            count +=1
            if count <= 20:  #不同的k不同的值
                templine+=line
            elif "#" in line:
                count=0
                templine+='#\n'
            else:continue
        f_w.write(templine)

for filename in file_list: #文件批量改名
    if '_50_' in filename: #mix为'_50',其他为‘_50_’
        newname = filename.replace('_50_','_20_') #针对其他的，不同的k修改后面的值
        #newname = filename.replace('_50', '_10')  # 针对Mix,不同的k修改后面的值
        os.rename(RootPath+ "\\" + filename,RootPath+ "\\" + newname)
        print(filename, '======>', newname)