# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib
import re
import time
import socket
import jsonShop

# 获取 BeautifulSoup对象
def getBsObj (url):
	browser = webdriver.PhantomJS()
	browser.get(url)
	time.sleep(10)
	bsObj = BeautifulSoup(browser.page_source, "html.parser")
	return bsObj

# 获取需要执行js 的页面 BeautifulSoup对象 
def getBsObjJs (url, js):
	browser = webdriver.PhantomJS()
	browser.get(url)
	time.sleep(10)
	print('js 执行开始')
	# js = "document.body.scrollTop=2400"
	# js = "var imgBox = document.getElementsByClassName('menucategory-categoryItem_3e27M'); var e = document.createEvent('MouseEvents'); e.initEvent('click', true, true); for (var i = 0; i < imgBox.length; i++) {(function(j){ setTimeout(function () {imgBox[j].dispatchEvent(e)}, 5000 * j)})(i);}"
	browser.execute_script(js)
	time.sleep(80)
	print('js 执行结束')
	bsObj = BeautifulSoup(browser.page_source, "html.parser")
	return bsObj