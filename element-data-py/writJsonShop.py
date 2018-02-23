# -*- coding: utf-8 -*-
import jsonShop
import json

# 写入json文件
def writeJsonFile (url, jsonFileUrl):
	textJson = jsonShop.getJsonDict(url)
	with open(jsonFileUrl, "w") as fw:
		json.dump(textJson, fw, indent=2)

# 写入json文件
def writeJsonFile2 (jsonText, jsonFileUrl):
	with open(jsonFileUrl, "w") as fw:
		json.dump(jsonText, fw, indent=2)

# 写入json文件
def writeListFile (listObj, jsonFileUrl):
	jsonText = jsonShop.getListObj(listObj)
	with open(jsonFileUrl, "w") as fw:
		json.dump(jsonText, fw, indent=2)