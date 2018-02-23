# -*- coding: utf-8 -*-
import imgShop

# 直接返回
def getReturnArr (imgUrlArr):
	return imgUrlArr

# 获取元素二次处理
def getShopFoodImg (imgUrlArr):
	arr = []
	for e in imgUrlArr:
		arr.append(e.find_all('img')[0])
	return arr

# 获取元素二次处理
def getNavImg (imgUrlArr):
	arr = []
	for e in imgUrlArr:
		imgElement = e.find_all('img')
		for img in imgElement:
			arr.append(img)
	return arr

# 二次封装
getFoodImgFn = imgShop.getImgFnJs("fooddetails-logo_2Q0S7", r"\/\w{2}\/.+?\?", getShopFoodImg)
# 二次封装
getLogoImgFn = imgShop.getImgFn("shop-header-2hPPi_0", r"\/\w{2}\/.+?\?", getReturnArr) 
# 二次封装
getNavImgFn = imgShop.getImgFn("mint-swipe-item", r"\/\w{2}\/.+?\?", getNavImg) 