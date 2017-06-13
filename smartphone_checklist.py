#!/usr/bin/env python3
#coding:utf-8
#检索关键词
#平台MT6276
MAKE=['CUSTOM_MODEM','#define USING_CLASS','MTK_FM_CHIP','MTK_BT_SUPPORT','MTK_DHCPV6C_WIFI','MTK_GPS_SUPPORT',\
'MTK_NFC_SUPPORT','MTK_ATV_CHIP','MTK_FM_SHORT_ANTENNA_SUPPORT','GEMINI','MTK_SHARED_SDCARD','MTK_DUAL_MIC_SUPPORT',\
'CONFIG_CUSTOM_KERNEL_LCM','CUSTOM_KERNEL_MAIN_LENS','CUSTOM_KERNEL_IMGSENSOR','CUSTOM_KERNEL_SUB_LENS',\
'CUSTOM_KERNEL_SUB_IMGSENSOR','sagereal_battery_capacity']
#后续如果想多增加宏可以在MAKE数组的末尾添加，同时也要在CHR的末尾添加描述，顺序必须一致！！
CHR=['频段/射频PA','内部PA型号','FM','BT','WIFI','GPS','NFC','ATV','FM share','SIM 卡(单卡/双卡）','T 卡','MIC(single/Dual)',\
'LCD 模组','后camera镜头','后camera IC','前camera镜头','前camera IC','电池参数']

num=len(MAKE)
#打开文件
str=input("请输入make文件完整地址:\n")
#str='D:\PROJECT\DL190\make\DL190_AX1811_SYM_GSM.mak'
f = open('checklist.txt', 'w')
#makefile=open(r"D:\PROJECT\11BW1308MP_SAGETEL60A_6464_11B_V40_GPRS_MMI_INT\make\UL280_T472_ET_GPRS.mak" )
makefile=open(str,'r',encoding='utf8')
j=0
line=makefile.readline()#一行行读入
while line !='' and line !=None:#循环读入并检索输出
#跳过注释语句和空语句
	j=0
	if line[0]=="#" or line[0]==' ' or line[0]=='\n' :
		line=makefile.readline()
		continue
#find的函数功能是查找指定的字符串并返回该字符串的起始位置 find(str,pos_start,pos_end)
	for i in range(1,num+1):
		if line.find(MAKE[i-1])==0:#开头精确搜索 模糊搜索 但匹配文字只需！=-1
			print(line,end='')
			f.write('\n'+CHR[i-1]+' :\n')
			f.write(line)
			line=makefile.readline()
			MAKE.pop(i-1)
			CHR.pop(i-1)
			num=num-1
			j=1
			break
	if j==0:
		line=makefile.readline()
makefile.close() 
f.close()
