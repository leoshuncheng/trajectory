import os,re,sys,scipy.stats as st

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(dirs)
        # print(files)
        return files
#上一次测试了mix的，可行，就把下面三个的文件夹清空了
beijing = 'D:\\trajectory_last\\两个数据集绘图数据文件合并\\beijing'#需要把北京全部的绘图数据放在这个文件夹
geolife = 'D:\\trajectory_last\\两个数据集绘图数据文件合并\\geolife'#需要把geolofe全部的绘图数据放在这个文件夹
merge = 'D:\\trajectory_last\\两个数据集绘图数据文件合并\\merge'#保持空的就行
'''
代码不需要改，上面三个目录准备好后直接执行就行了，结果在merge文件中
'''

FileNames = file_name(beijing)#获取文件夹包含的绘图数据文件名,两个数据集是一样的，只需要一个
#geolifeFileNames = file_name(geolife)

for FileName in FileNames:
    newString = ''
    file1 = open(beijing + '\\' + FileName,'r')
    file2 = open(geolife + '\\' + FileName,'r')
    lines_1 = file1.readlines()
    lines_2 = file2.readlines()
    newString += lines_1[0]
    list = [1,2,3]
    for lineindex in list:#一共三行数字
        if lineindex == 1:
            newString+='10  '
        elif lineindex == 2:
            newString+='20  '
        elif lineindex == 3:
            newString+='50  '
        line1 = lines_1[lineindex].split('  ')
        line2 = lines_2[lineindex].split('  ')
        for i in range(1,16):
            av = (float(line1[i])+float(line2[i]))/2.0
            newString+=str(av)+'  '
        newString+='\n'
    print(newString)
    output = open(merge+'\\'+FileName,'w')
    output.write(newString)












