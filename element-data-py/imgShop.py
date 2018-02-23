# -*- coding: utf-8 -*-
import urllib
import re
import socket
import bsShop
import fileShop

def getImgUrlArrJs (url, js, condition, callBackGetImgURl):
	bsObj = bsShop.getBsObjJs(url, js)
	imgUrlArr = bsObj.find_all(attrs={"class": condition})
	imgUrlArr = callBackGetImgURl(imgUrlArr)
	return imgUrlArr

def getImgUrlArr (url, condition, callBackGetImgURl):
	bsObj = bsShop.getBsObj(url)
	imgUrlArr = bsObj.find_all(attrs={"class": condition})
	imgUrlArr = callBackGetImgURl(imgUrlArr)
	return imgUrlArr

def getImgNameArr (imgUrlArr, p1):
	pattern1 = re.compile(p1) # 编译这段正则表达式
	imgNameArr = []
	# for 循环处理
	for element in imgUrlArr:
		srcStr = dict(element.attrs)['src']
		matcher1 = re.search(pattern1,srcStr)
		srcStr = matcher1.group(0)
		# 正则是变化的
		srcStr = re.sub(r'\/\w{2}\/', '', srcStr)
		srcStr = re.sub(r'\?', '', srcStr)
		imgNameArr.append(srcStr)
	return imgNameArr

def getImgFnJs (condition, p1, callBackGetImgURl):
	def auto_down(url,filename):
		try:
			urllib.request.urlretrieve(url,filename)
		except socket.timeout:
			count = 1
			while count <= 5:
				try:
					urllib.request.urlretrieve(url,filename)
					break
				except socket.timeout:
					err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
					print(err_info)
					count += 1
			if count > 5:
				print("downloading picture fialed!")
	def getImg(url1, url2, js):
		imgUrlArr = getImgUrlArrJs(url1, js, condition, callBackGetImgURl)
		imgNameArr = getImgNameArr(imgUrlArr, p1)
		for i in range(0, len(imgUrlArr)):
			srcStr = dict(imgUrlArr[i].attrs)['src']
			imgName = imgNameArr[i].split('.')
			img_src = srcStr
			# 地址是变化的
			print(url2  + imgName[0] + '.' + imgName[1])
			fileShop.getMakedirsFil(url2)
			auto_down(img_src, r'' + url2 + imgName[0] + '.' + imgName[1])
	return getImg

def getImgFn (condition, p1, callBackGetImgURl):
	def auto_down(url,filename):
		try:
			urllib.request.urlretrieve(url,filename)
		except socket.timeout:
			count = 1
			while count <= 5:
				try:
					urllib.request.urlretrieve(url,filename)
					break
				except socket.timeout:
					err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
					print(err_info)
					count += 1
			if count > 5:
				print("downloading picture fialed!")
	def getImg(url1, url2):
		imgUrlArr = getImgUrlArr(url1, condition, callBackGetImgURl)
		imgNameArr = getImgNameArr(imgUrlArr, p1)
		for i in range(0, len(imgUrlArr)):
			srcStr = dict(imgUrlArr[i].attrs)['src']
			imgName = imgNameArr[i].split('.')
			img_src = srcStr
			if img_src.find('https:') == -1 :
				img_src = 'https:' + img_src
			# 地址是变化的
			print('' + url2 + imgName[0] + '.' + imgName[1])
			fileShop.getMakedirsFil(url2)
			auto_down(img_src, r'' + url2 + imgName[0] + '.' + imgName[1])
	return getImg