# -*- coding: utf-8 -*-
import os

def getFileNot (imgAddress):
	if os.path.exists(imgAddress):
		return 1
	else:
		return 2

def getMakFile (imgAddress):
	try:
		os.makedirs(imgAddress)
	except BaseException:
		print('Error: 创建文件夹出错, 可能已存在' + str(imgAddress))

def getReadAndMakedirs (imgAddress):
	fileNot = getFileNot(imgAddress)
	makFile = getMakFile(imgAddress)
	if fileNot == 2 and imgAddress.find('.', 1) > -1:
		getMakFile(imgAddress)

def getMakedirsFil (imgAddress):
	fileNot = getFileNot(imgAddress)
	if fileNot == 2:
		getMakFile(imgAddress)