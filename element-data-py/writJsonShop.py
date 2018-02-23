# -*- coding: utf-8 -*-
import jsonShop
import json

def writeJsonFile (url, jsonFileUrl):
	textJson = jsonShop.getJsonDict(url)
	with open(jsonFileUrl, "w") as fw:
		json.dump(textJson, fw, indent=2)

def writeJsonFile2 (jsonText, jsonFileUrl):
	with open(jsonFileUrl, "w") as fw:
		json.dump(jsonText, fw, indent=2)

def writeListFile (listObj, jsonFileUrl):
	jsonText = jsonShop.getListObj(listObj)
	with open(jsonFileUrl, "w") as fw:
		json.dump(jsonText, fw, indent=2)