import datetime,time,math
import numpy as np
import os,re,sys,scipy.stats as st

np.random.seed(1337)

result_folder_name = "geolife_last_result/"
folder_name = 'geolife_last/50after/'
#三个文件：原始的轨迹距离Geolife、spearman文件GeolifeResult（空的）、还有一个画图数据文件，这里没用到
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(dirs)
        print(files)
        return files

def dir_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(dirs)
        print(files)
        return dirs

def person_mul(data1,data2):#值的计算
    num = len(data1)
    sum_data1 = sum(data1)
    sum_data2 = sum(data2)
    data1_mean = float(sum_data1 + 0.0) / num
    data2_mean = float(sum_data2 + 0.0) / num
    sumTop = 0.0
    sumBottom = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(num):
        sumTop += (data1[i] - data1_mean) * (y[i] - data2_mean)
    for i in range(num):
        x_pow += math.pow(data1[i] - data1_mean, 2)
    for i in range(num):
        y_pow += math.pow(data2[i] - data2_mean, 2)
    sumBottom = math.sqrt(x_pow * y_pow)
    p = sumTop / sumBottom
    return p
def all_spearman(data):#该文件所有的计算
    num = len(data)
    result = st.spearmanr(data)
    print(result)
    result = result[0]
    num = len(result)
    for i in range(num):
        for j in range(num):
            print(str(i) + "," + str(j) + ":" + str(result[i][j]))
    return result

def load(dir,path):
    #print(folder_name+"/"+dir+path)
    f = open(folder_name+dir+"/"+path)
    if not os.path.exists(result_folder_name):
        os.makedirs(result_folder_name)
    if not os.path.exists(result_folder_name+folder_name):
        os.makedirs(result_folder_name+folder_name)
    if not os.path.exists(result_folder_name+folder_name+dir+"/"):
        print(result_folder_name+folder_name+dir+"/")
        os.makedirs(result_folder_name+folder_name+dir+"/")
    #elif not os.path.exists(result_folder_name+folder_name+dir+"/"+):

    f2=open(result_folder_name+folder_name+dir+"/"+path,'w')
    data = []
    i = 0
    mid = []
    for line in f:
        words = line.split(' ', 1)
        words = words[0].strip()
        if (words== '#'):
            i += 1
            data.append(mid)
            mid = []
        else:
            mid.append(words)

        #f2.write(now_str)
    result = st.spearmanr(data)
    result = result[0]
    num = len(result)
    count = 0.0
    for i in range(num):
        for j in range(num):
            if(i!=j):
                count+=result[i][j]

    ava = count/(num*(num-1))
    f2.write(str(ava)+"\n")
    for i in range(num):
        for j in range(num):
            f2.write(str(i) + "," + str(j) + ":" + str(result[i][j])+"\n")
    f.close()
    f2.close()



dirs=dir_name(folder_name)
print(dirs)
for dir in dirs:
    files = file_name(folder_name+dir+"/")
    for file in files:
        if (file != '.DS_Store'):
            load(dir,file)

