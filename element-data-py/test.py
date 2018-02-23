# -*- coding: utf-8 -*-
import urllib
import re
import socket
import bsShop
import fileShop
import time 

def getImgUrlArr (url, condition, callBackGetImgURl):
	bsObj = bsShop.getBsObj(url)
	imgUrlArr = bsObj.select(condition)
	# imgUrlArr = bsObj.find_all(name="img", attrs={"class": condition})
	print(imgUrlArr)
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
			# 地址是变化的
			print(url2 + imgName[0] + '.' + imgName[1])
			fileShop.getMakedirsFil(url2)
			auto_down(img_src, r'' + url2 + imgName[0] + '.' + imgName[1])
	return getImg

def getReturnArr (imgUrlArr):
	return imgUrlArr

getLogoImgFn = getImgFn('img[class="shop-header-2hPPi_0"]', r"\/\w{2}\/.+?\?", getReturnArr) 



url = 'https://h5.ele.me/shop/#geohash=ws105rz9smwm&id=1329266&s_type=0&rank_id=20ff7cb9b1d149bea9548742817abcc3'

getLogoImgFn('https://h5.ele.me/shop/#geohash=ws105rz9smwm&id=1329266&s_type=0&rank_id=20ff7cb9b1d149bea9548742817abcc3','E:/Python/eleme-data-gain/img/logo/')


# -----------------------------------------------------------------------------------------
# import re
# import json

# def getJsonObj(json_text):
# 	text = json_text
# 	text = json.dumps(text)
# 	text = json.loads(text)
# 	textJson = json.loads(text)
# 	return textJson

# def writeJsonFile2 (jsonText, jsonFileUrl):
# 	with open(jsonFileUrl, "w") as fw:
# 		json.dump(jsonText, fw, indent=2)










# -----------------------------------------------------------------------------------------
# p1 = r"offset=.+?" 	
# pattern1 = re.compile(p1) 
# matcher1 = re.search(pattern1,url)

# a = [1,2,3,{'4': 5, '6': 7}]



# print(type(textJson))
# writeJsonFile2(textJson, 'a.json')


