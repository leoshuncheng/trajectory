import datetime,time,math
import numpy as np
import os,re,sys,scipy.stats as st

#read_dir_name='D:\trajectoryPIC\Geolife\sp_only'  'add_noise_1pct_2d',

file_houzhui=[
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

for filename in file_houzhui:
    # 将文件读取到内存中
    with open("D:\\trajectoryPIC\\Geolife\\sp_tem\\" + filename+'.plt', "r", encoding="utf-8") as f:
        lines = f.readlines()
    # 写的方式打开文件
    with open("D:\\trajectoryPIC\\Geolife\\sp_tem\\" + filename+'.plt', "w", encoding="utf-8") as f_w:
        for line in lines:
            if "#set bmargin 10" in line:
                #line=line.replace("add_noise_1pct_2d",filename)
                # 替换
                #line = line.replace("20","30")
                line="set key font \"Time-Roman,30\"\nset key spacing 3.50\nset key width 6.9\n"
                #line = "set xtic rotate by -45 scale 0 font \"Time-Roman,20\"\nset ytics font \"Time-Roman,20\"\n"
                #line="'' u 8 ti col,'' u 9 ti col,'' u 13 ti col,'' u 15 ti col\n"
                #line="set xlabel \"k\" font \"Time-Roman,20\"\n"
            f_w.write(line)

