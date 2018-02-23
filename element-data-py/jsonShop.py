# -*- coding: utf-8 -*-
import bsShop
import json

# 将json数据更改为json对象
def getJsonObj(json_text):
	text = json_text
	text = text.encode('utf8')
	textJson = json.loads(text)
	return textJson

# 获取json对象
def getJsonDictJs(url, js):
	bsObj = bsShop.getBsObjJs(url, js)
	textJson = getJsonObj(bsObj.get_text())
	return textJson
# 获取json对象
def getJsonDict(url):
	bsObj = bsShop.getBsObj(url)
	textJson = getJsonObj(bsObj.get_text())
	return textJson

# 将list数据更改为json对象
def getListObj(listObj):
	text = listObj
	text = json.dumps(text)
	textJson = json.loads(text)
	return textJson