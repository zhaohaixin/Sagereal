#-*- coding: UTF-8 -*- 。
#检索关键词
#平台MT6276
import os
import zipfile
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
zip_dir(r'/home/zhaohaixin/桌面/修改',r'/home/zhaohaixin/桌面/xiugai.zip')