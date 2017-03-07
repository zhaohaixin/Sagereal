import os
import time
import glob

path = input('请输入根目录路径（所有文件夹以1,2,3,4..命名）：')
Type=['D65','CWF','TL84','A','H','DF','DNP','SUN']#在此处添加不同情景下的光，从左到右为拍摄顺序
if input(list(Type)+'(请输入 y or n)'+':')!='y':
    exit()
#path='/home/zhaohaixin/桌面/实验/'
Golden=input('请输入Golden文件夹名称：')
# path = '/home/zhaohaixin/桌面/500D'
# #path='/home/zhaohaixin/桌面/实验/'
# Golden=3-


name_time_list = []
phonenum=len(os.listdir(path))#input('请输入样机数量:')
for num in range(1,phonenum+1):
    name_time_list = []
    ##按时间顺序获取.raw文件路径
    for filename in glob.glob(path+'/%d/CameraEM/*.raw'%num):#填写路径
        name_time_list.append((time.ctime(os.path.getmtime(filename)), filename))
    name_time_list.sort()
    #查找文件是否符合对应的数量
    if len(name_time_list)!=len(Type):
        print('文件夹\'%d\':文件数量或者格式不正确'%num)
        exit()
    #修改文件名字
    if str(num)==Golden:
        for i in range(len(name_time_list)):
            name=os.path.split(name_time_list[i][1])#分离文件路径和名字
            os.rename(name_time_list[i][1], name[0]+'/'+'Golden-%s__'%Type[i]+name[1].split('__',1)[1])
        continue
    for i in range(len(name_time_list)):
            name=os.path.split(name_time_list[i][1])#分离文件路径和名字
            os.rename(name_time_list[i][1], name[0]+'/'+'Unit0%d-%s__'%(num,Type[i])+name[1].split('__',1)[1])


#Capture20100101-000240ISOAutopure__3264 * 2248_10_0.raw
