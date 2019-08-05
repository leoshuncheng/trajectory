import datetime,time,math
import numpy as np
import os,re,sys,scipy.stats as st
#折线图
def dir_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return dirs

print(dir_name("spearnman_result/"))
dirs = dir_name("spearnman_result/")
ks = ['10','20','50']
filenames=['DTW','EDR_01','EDwP','ERP','LIP','LCSS_01','OWD',
           'PDTW','TID','EUCLIDEAN','HAUSDORFF','MERGE',
           'FRECHET','STED','STLCSS_01','STLCSS-SIGMOID_01','STLIP','TSJOIN_05']
f2=open("pic_result/data",'w')
for k in ks:
    for filename in filenames:
        f=open("spearnman_result/"+k+"/"+filename+"_"+k)
        lines = f.readlines()
        line=lines[0].rstrip('\n')
        print(line)
        f2.write(line+"  ")
    f2.write("\n")
