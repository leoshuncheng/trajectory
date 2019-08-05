import datetime,time,math
import numpy as np
import os,re,sys,scipy.stats as st
#折线图
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
dirs = dir_name("spearnman_result/")
ks = ['10','20','50']
filenames=['DTW']
f2=open("pic_result/dataDTW",'w')
region = 'Region  '
# files=file_name("spearnman_result/"+'10'+"after/"+"DTW"+"_"+'10')
# print(files)
file_houzhui=['add_noise_1pct_2d',
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

for file1 in file_houzhui:
    region += file1.replace('_','-')
    region += '  '
f2.write(region+'\n')

for filename in filenames:
    #line = k+'  '
    #f2.write(k+'  ')
    for k in ks:
        f2.write(k + '  ')
        #files=file_name("spearnman_result/"+k+"after/"+filename+"_"+k)
        #print(files)
        for file in file_houzhui:
            # region+=file[7:-1]
            # region+='  '
            f = open("spearnman_result/" +k+"after/"+filename+"_"+k+"/"+filename+"_"+k+"_"+file)
            lines = f.readlines()
            firstline = lines[0].rstrip('\n')+'  '
            #line=line+firstline
            f2.write(firstline)
        f2.write("\n")


