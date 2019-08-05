import datetime,time,math
import numpy as np
import shutil
import os,re,sys,scipy.stats as st

Rootpath="G:\\电科论文\\Geolife Trajectories 1.3\\Data"
def dir_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return dirs

def file_names(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return files

filenames=dir_name(Rootpath)
# print(file_names(Rootpath+"\\000\\Trajectory"))

for filename in filenames:
    allfiles=file_names(Rootpath+"\\"+filename+"\\Trajectory")
    for allfile in allfiles:
        shutil.copy(Rootpath+"\\"+filename+"\\Trajectory\\"+allfile,"G:\\电科论文\\Geolife Trajectories 1.3\\alldata")




