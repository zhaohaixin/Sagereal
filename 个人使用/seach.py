import os


def gci(filepath):
  #遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for fi in files:
    fi_d = os.path.join(filepath, fi)
    if os.path.isdir(fi_d):
      gci(fi_d)
    else:
      location = os.path.join(filepath, fi_d)
      if os.path.basename(location) == 'ProjectConfig.mk':
        address.append(location)
        print(location)
      #print os.path.join(filepath, fi_d)


def search(filepath, string, function):
  address = []
  soucefile = open(filepath)
  line = soucefile.readline()
  while line != ''and line ！ = None:
    if line[0] == "#"or line[0] == ' 'or line[0] == '\n':
      line = soucefile.readline()
      continue
    if line.find(string) == 0:# 模糊搜索
      address.append()
#递归遍历/root目录下所有文件
PATH = input('需要寻找根路径：')
FILENAME = input('需要寻找的文件：')
STRING = input('需要寻找的关键词：')
STRING1 = input('替换的内容：')
gci(r'/home/zhaohaixin/sagerael/ALPS.KK1.MP7.V1.22_SR72_W_KK')
