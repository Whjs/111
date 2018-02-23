# -*- coding: utf-8 -*-
import os

# 判断文件是否存在
def getFileNot (imgAddress):
	if os.path.exists(imgAddress):
		return 1
	else:
		return 2

# 创建文件
def getMakFile (imgAddress):
	try:
		os.makedirs(imgAddress)
	except BaseException:
		print('Error: 创建文件夹出错, 可能已存在' + str(imgAddress))

# 创建文件  当文件不存在的时候就创建
def getReadAndMakedirs (imgAddress):
	fileNot = getFileNot(imgAddress)
	makFile = getMakFile(imgAddress)
	if fileNot == 2 and imgAddress.find('.', 1) > -1:
		getMakFile(imgAddress)

# 创建 文件
def getMakedirsFil (imgAddress):
	fileNot = getFileNot(imgAddress)
	if fileNot == 2:
		getMakFile(imgAddress)