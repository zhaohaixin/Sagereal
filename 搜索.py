import os
def do_dir(d, file):
    for f in os.listdir(d):   #列出目录下的所以文件及目录
        f = os.path.join(d, f)  #通过os.path.join()函数，把两个路径合成一个时
        if os.path.isfile(f):    #判断是否是文件
            if os.path.basename(f)[1] == 'ProjectConfig.mk: #判断是否是需要的文件类型
                print(os.path.abspath(f)) #打印出绝对路径
        else:  #如果是目录，递归进行
            do_dir(f, file) 
pwd_path = input('请输入绝对目录：')
print('你选择的目录是(如/home/name)：%s'%pwd)
file = input('请输入想寻找的文件类型(如py或者html等)：')
do_dir(pwd, file)
