#!/usr/bin/env python3
import sys
import urllib.request
from bs4 import BeautifulSoup
page = urllib.request.urlopen('https://www.cnblogs.com/Axi8/p/5757270.html')#打开网页
#htmlcode = page.read()#读取页面源码
htmlcode=BeautifulSoup(page)
print (sys.version)
print (htmlcode)#在控制台输