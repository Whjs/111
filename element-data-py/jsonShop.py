# -*- coding: utf-8 -*-
import bsShop
import json

def getJsonObj(json_text):
	text = json_text
	text = text.encode('utf8')
	textJson = json.loads(text)
	return textJson

def getJsonDictJs(url, js):
	bsObj = bsShop.getBsObjJs(url, js)
	textJson = getJsonObj(bsObj.get_text())
	return textJson

def getJsonDict(url):
	bsObj = bsShop.getBsObj(url)
	textJson = getJsonObj(bsObj.get_text())
	return textJson

def getListObj(listObj):
	text = listObj
	text = json.dumps(text)
	textJson = json.loads(text)
	return textJson