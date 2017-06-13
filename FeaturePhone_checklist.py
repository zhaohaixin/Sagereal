#!/usr/bin/env python3
#coding:utf-8
#检索关键词
#平台MT6276
MAKE=['BOARD_VER','PLATFORM','RF_MODULE','PMIC','CLASSK_CHARGEPUMP_SUPPORT','RF_PARA_CUSTOM',\
'FM_RADIO_CHIP','BLUETOOTH_SUPPORT','WIFI_SUPPORT','GPS_SUPPORT','NFC_SUPPORT','GEMINI','MSDC_CARD_SUPPORT_TYPE',\
'DUAL_MIC_SUPPORT','ATV_SUPPORT','MAIN_LCD_SIZE','CMOS_SENSOR','AFC_VCXO_TYPE','EXT_CLOCK',\
'SENSOR_TYPE','SECOND_CMOS_SENSOR','SENSOR_TYPE_SUB','CMOS_SENSOR_SUB','SR_CHECK_BATT_TEMP','INTERNAL_ANTENNAL_SUPPORT','SAGETEL_PRODUCT_NAME']
#后续如果想多增加宏可以在MAKE数组的末尾添加，同时也要在CHR的末尾添加描述，顺序必须一致！！

CHR=['主板版本','平台','频段/射频PA','PMIC','音频PA','射频参数','FM','蓝牙','WIFI','GPS','NFC','SIM 卡(单卡/双卡）',\
'T 卡','MIC(single/Dual)','ATV','LCD 尺寸/分辨率','后camera型号','AFC_VCXO_TYPE','EXT_CLOCK',\
'后camera类型（YUV,RAW,JPEG)','兼容camera型号','前camera类型（YUV,RAW,JPEG)','前cmaera型号','SR_CHECK_BATT_TEMP','FM share','产品软件版本']

num=len(MAKE)
#打开文件
str=input("请输入make文件完整地址:\n")
#str='D:\PROJECT\DL190\make\DL190_AX1811_SYM_GSM.mak'
f = open('checklist.txt', 'w')
#makefile=open(r"C:\Users\Administrator\Desktop\办公脚本\脚本\NL03_X241_ZTE_RU_VELCOM_HSPA.mak" )
makefile=open(str,'r')
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
