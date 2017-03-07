#!/usr/bin/python  
#coding=utf-8  
import os  
from time import sleep  
def camera():
	os.system('adb shell input keyevent 82') #解锁屏幕
	#os.system('adb shell screenrecord --time-limit 4 /sdcard/demo.mp4')  #录屏
	#sleep(1)
	os.system('adb shell am start -n com.google.android.GoogleCamera/com.android.camera.CameraLauncher')  #打开camera
	#os.system('adb shell screencap /sdcard/cameratest/%d.png'%i) 
	print('次数：%d'%i)
	sleep(4)
	os.system('adb shell  am force-stop com.google.android.GoogleCamera') #杀死camera进程
	os.system('adb shell input keyevent 223') #手机进入休眠
	
i=1
while 1:
	camera()
	i=i+1
	sleep(8)
	print('删除这次数据?')#如果否直接命令行ctrl+c
	sleep(40)
	#os.system('adb shell rm sdcard/demo.mp4') #删除文件夹
	
	

