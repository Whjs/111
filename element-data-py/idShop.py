# -*- coding: utf-8 -*-
import re
import jsonShop
import writJsonShop
import json

def getIdList(itemDict):
	items = itemDict['items']
	idList = []
	for i in range(0, len(items)):
		try:
			idList.append(items[i]['restaurant']['id'])
		except BaseException:
			print('没有id')
	return idList

def getShopIdListJs(url, js):
	itemDict = jsonShop.getJsonDictJs(url, js)
	idList = getIdList(itemDict)
	return idList

def getShopIdList(url):
	itemDict = jsonShop.getJsonDict(url)
	idList = getIdList(itemDict)
	# p1 = r"offset=.+?" 	
	# pattern1 = re.compile(p1) 
	# matcher1 = re.search(pattern1,url)
	# print(matcher1.group(0))
	# # 获取主页店铺信息 URl 以及 数据地址
	# writJsonShop.writeJsonFile2(itemDict, './data/restaurants/restaurants-' + str(matcher1.group(0)) + '.json')
	return idList

def getShopIdJson (fileUrl):
	myfile=open(fileUrl,'r')
	result=json.load(myfile)
	myfile.close()
	return result


# 获取店铺 Id-----------------------
# shopIds = []
# for i in range(0, 3):
# 	urlN = i * 8
# 	url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=22.54286&longitude=114.059563&offset='+ str(urlN) +'&limit=8&extras[]=activities&extras[]=tags&extra_filters=home&rank_id=20ff7cb9b1d149bea9548742817abcc3&terminal=h5'
# 	shopIdList = idShop.getShopIdList(url)
# 	shopIds.extend(shopIdList)
# shopIds.sort()
# print(shopIds)


# writJsonShop.writeListFile(shopIds, './data/shopIdList/shopIds.json')

