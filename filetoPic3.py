import datetime,time,math
import numpy as np
import os,re,sys,scipy.stats as st
#折线图数据生成
def dir_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return dirs

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return files

#print(dir_name("spearnman_result/"))
dirs = dir_name("geolife_lastResult/")
ks = ['10','20','50']
#filenames=['DTW']

#f2=open("pic_result/add_noise_1pct_2d",'w')
region = 'Region  '
# files=file_name("spearnman_result/"+'10'+"after/"+"DTW"+"_"+'10')
# print(files)
filenames=['DTW','EDR_01','ERP','LIP','LCSS_01','OWD',
           'PDTW','EUCLIDEAN','MERGE',
           'FRECHET','STED','STLCSS_01','STLIP','TSJOIN_05','EDwP']
# file_houzhui=['MixOfAllTransformation'] #mix专用
file_houzhui=['add_noise_1pct_2d',  #其他专用
              'add_noise_1pct_5d',
              'add_noise_1pct_10d',
              'add_noise_5pct_2d',
              'add_noise_5pct_5d',
              'add_noise_5pct_10d',
              'add_pts_25pct',
              'add_pts_50pct',
              'add_pts_100pct',
              'add_pts_200pct',
              'delete_pts_10pct',
              'delete_pts_20pct',
              'delete_pts_40pct',
              'delete_pts_80pct',
              'dif_time_rate_1pts',
              'dif_time_rate_2pts',
              'dif_time_rate_4pts',
              'dif_time_rate_8pts',
              'scale_25pct',
              'scale_50pct',
              'scale_200pct',
              'scale_400pct',
              'time_scale_25pct',
              'time_scale_50pct',
              'time_scale_200pct',
              'time_scale_400pct']

for file0 in file_houzhui:
    region = 'Region  '
    f1 = open("lastpic_Geolife/"+file0, 'w')
    for file1 in filenames:
        if file1 == 'EUCLIDEAN':
            region += 'ED'
        elif file1 == 'MERGE':
            region += 'MD'
        elif file1 == 'TSJOIN_05':
            region += 'STLC'
        else:
            region += file1.rstrip('_01')
        region += '  '
    f1.write(region + '\n')
    f1.close()


for file in file_houzhui:
    #line = k+'  '
    #f2.write(k+'  ')
    f2 = open("lastpic_Geolife/" + file, 'a')
    for k in ks:
        f2.write(k + '  ')
        #files=file_name("spearnman_result/"+k+"after/"+filename+"_"+k)
        #print(files)
        for filename in filenames:
            f = open("geolife_lastResult/" +k+"after/"+filename+"_"+k+"/"+filename+"_"+k+"_"+file)#正常的使用这个
            #f = open("BeijingMixResult/" + k + "after/" + filename + "_" + k + file)#仅仅适用Mix
            lines = f.readlines()
            firstline = lines[0].rstrip('\n')+'  '
            #line=line+firstline
            f2.write(firstline)
        f2.write("\n")


