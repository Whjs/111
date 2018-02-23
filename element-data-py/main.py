# -*- coding: utf-8 -*-
import holdImgShop
import idShop
import writJsonShop
import json

# 获取店铺 Id-----------------------
shopIds = idShop.getShopIdJson('./data/shopIdList/shopIds.json')

# 获取店铺 Id-----------------------

js = "var imgBox = document.getElementsByClassName('menucategory-categoryItem_3e27M'); var e = document.createEvent('MouseEvents'); e.initEvent('click', true, true); for (var i = 0; i < imgBox.length; i++) {(function(j){ setTimeout(function () {imgBox[j].dispatchEvent(e)}, 5000 * j)})(i);}"


holdImgShop.getNavImgFn('https://h5.ele.me/msite/', './img/navImg/')




# 获取店铺信息 list---------------------------------
shop = []
shopRatings = []

for i in range(0, len(shopIds)):
	offsetN = i * 8;
	shopIdStr = str(shopIds[i])
	shopItem = {}
	shopItem['item'] = shopIds[i]
	# 获取店铺信息 URl 以及 数据地址
	shopItem['infoUrl'] = 'https://h5.ele.me/restapi/shopping/restaurant/' + shopIdStr +  '?extras[]=activities&extras[]=albums&extras[]=license&extras[]=identification&extras[]=qualification&terminal=h5&latitude=22.54286&longitude=114.059563'
	shopItem['infoAddress'] = './data/shop/infomation/infomation-' + shopIdStr + '.json'

	# 获取店铺左侧导航 URl 以及 数据地址
	shopItem['menuUrl'] = 'https://h5.ele.me/restapi/shopping/v2/menu?restaurant_id=' + shopIdStr
	shopItem['menuAddress'] = './data/shop/menu/' + shopIdStr + '.json'

	# 获取店铺 URL 以及 图片保存地址
	shopItem['foodImgUrl'] = 'https://h5.ele.me/shop/#geohash=ws105rz9smwm&id='+ shopIdStr +'&s_type=0&rank_id=20ff7cb9b1d149bea9548742817abcc3'
	shopItem['foodImgAddress'] = 'E:/Python/eleme-data-gain/img/shop/' + shopIdStr + '/'
	# 获取店铺 URL 以及 logo图片保存地址
	shopItem['logoImgUrl'] = 'https://h5.ele.me/shop/#geohash=ws105rz9smwm&id='+ shopIdStr +'&s_type=0&rank_id=20ff7cb9b1d149bea9548742817abcc3'
	shopItem['logoImgAddress'] = 'E:/Python/eleme-data-gain/img/logo/'
	for j in range(0, 3):
		urlN = 8 * i
		shopRatingsItem = {}
		shopRatingsItem['item'] = shopIds[i]
		# 获取店铺评论 URl 以及 数据地址
		shopRatingsItem['ratingsUrl'] = 'https://h5.ele.me/restapi/shopping/v2/menu?restaurant_id=' + shopIdStr + '&offset='+ str(urlN) +'&limit=8'
		shopRatingsItem['ratingsAddress'] = './data/shop/ratings/' + shopIdStr + '-' + str(j) + '.json'
		shopRatings.append(shopRatingsItem)
	shop.append(shopItem)

		
	
# print(shopItem)
# print(len(shop))

for i in range(0, len(shop)):
	print('shop-' + str(i))
	获取店铺信息
	writJsonShop.writeJsonFile(shop[i]['infoUrl'], shop[i]['infoAddress'])
	获取店铺左侧导航
	writJsonShop.writeJsonFile(shop[i]['menuUrl'], shop[i]['menuAddress'])
	获取店铺食品图片
	holdImgShop.getFoodImgFn(shop[i]['foodImgUrl'], shop[i]['foodImgAddress'], js)
	获取店铺Logo图片
	holdImgShop.getLogoImgFn(shop[i]['logoImgUrl'], shop[i]['logoImgAddress'])

for i in range(0, len(shopRatings)):
	print('shopRatings-' + str(i))
	# 获取店铺评论
	writJsonShop.writeJsonFile(shopRatings[i]['ratingsUrl'], shopRatings[i]['ratingsAddress'])



