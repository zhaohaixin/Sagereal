#!/usr/bin/env python3
#coding:utf-8
import os
import zipfile
NAME=input('项目名：')
NUM=int(input('创建版本数：'))
PATH=input('存放文件地址:')
COMMIT=[]
while NUM>0:
    COMMIT.append(input('请输入commit号：'))
    NUM=NUM-1
for commit in COMMIT:
    os.system('git clean -df;git reset --hard %s' %commit)
    os.system('cd alps;./mk %s new' %NAME)
    zip_dir(os.getcwd()+NAME,PATH+NAME+'_%s.zip'%commit[:6])

def zip_dir(dirname,zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else :
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))
         
    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar,arcname)
    zf.close()



    

