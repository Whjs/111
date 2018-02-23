# -*- coding: utf-8 -*-
import imgShop


def getReturnArr (imgUrlArr):
	return imgUrlArr

def getShopFoodImg (imgUrlArr):
	arr = []
	for e in imgUrlArr:
		arr.append(e.find_all('img')[0])
	return arr

def getNavImg (imgUrlArr):
	arr = []
	for e in imgUrlArr:
		imgElement = e.find_all('img')
		for img in imgElement:
			arr.append(img)
	return arr

getFoodImgFn = imgShop.getImgFnJs("fooddetails-logo_2Q0S7", r"\/\w{2}\/.+?\?", getShopFoodImg)

getLogoImgFn = imgShop.getImgFn("shop-header-2hPPi_0", r"\/\w{2}\/.+?\?", getReturnArr) 

getNavImgFn = imgShop.getImgFn("mint-swipe-item", r"\/\w{2}\/.+?\?", getNavImg) 