#!/usr/bin/env python3
#coding:utf-8
#检索关键词
#平台MT6276
MAKE=['BOARD_VER','PLATFORM','RF_MODULE','PMIC','CLASSK_CHARGEPUMP_SUPPORT','RF_PARA_CUSTOM',\
'FM_RADIO_CHIP','BLUETOOTH_SUPPORT','WIFI_SUPPORT','GPS_SUPPORT','NFC_SUPPORT','GEMINI','MSDC_CARD_SUPPORT_TYPE',\
'DUAL_MIC_SUPPORT','ATV_SUPPORT','MAIN_LCD_SIZE','CMOS_SENSOR','RF_PARA_CUSTOM','AFC_VCXO_TYPE','EXT_CLOCK','SECOND_CMOS_SENSOR',\
'SENSOR_TYPE','SECOND_CMOS_SENSOR','SENSOR_TYPE_SUB','CMOS_SENSOR_SUB','SR_CHECK_BATT_TEMP']
num=len(MAKE)
#打开文件
str=input("请输入make文件完整地址:\n")
f = open('checklist.txt', 'w')
#makefile=open(r"D:\PROJECT\11BW1308MP_SAGETEL60A_6464_11B_V40_GPRS_MMI_INT\make\UL280_T472_ET_GPRS.mak" )
makefile=open(str)
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
			f.write(line)
			line=makefile.readline()
			MAKE.pop(i-1)
			num=num-1
			j=1
			break
	if j==0:
		line=makefile.readline()
makefile.close() 
f.close()
