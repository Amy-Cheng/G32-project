import requests
import pandas as pd
import json
import time
from datetime import datetime, timedelta
import scrapy
#url = "https://www.twse.com.tw/fund/T86?response=json&date={y}{m:02d}{d:02d}&selectType=ALLBUT0999&_=1577233837182"
#https://www.twse.com.tw/fund/T86?response=json&date=20191224&selectType=ALLBUT0999&_=1577233837182

date1 = input()
sid = input("股票代碼：")
three = []  # 用來儲存往前推三天的三大法人買賣超資料

def workday(date):  # 判斷是否為工作日
	global json_data
	dtnb = {'response': 'json', 'date': date, 'selectType': 'ALLBUT0999', '_' : '1577233837182'}
	json_data=requests.get("https://www.twse.com.tw/fund/T86", dtnb).json()
	if json_data == {'stat': '很抱歉，沒有符合條件的資料!'}:
		return False
	else:
		return json_data


def show_data(json_data):
	global data
	columns= ["證券代號","證券名稱","外陸資買進股數(不含外資自營商)","外陸資賣出股數(不含外資自營商)",
	"外陸資買賣超股數(不含外資自營商)","外資自營商買進股數","外資自營商賣出股數","外資自營商買賣超股數",
	"投信買進股數","投信賣出股數","投信買賣超股數","自營商買賣超股數","自營商買進股數(自行買賣)",
	"自營商賣出股數(自行買賣)","自營商買賣超股數(自行買賣)","自營商買進股數(避險)",
	"自營商賣出股數(避險)","自營商買賣超股數(避險)","三大法人買賣超股數"]

	data = pd.DataFrame(json_data['data'],columns=columns)
	data = data[["證券代號","外陸資買賣超股數(不含外資自營商)","外資自營商買賣超股數",
	"投信買賣超股數","自營商買賣超股數","三大法人買賣超股數"]]
	data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: x.replace(",", ""))
	data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: int(x))
	data.iloc[:, 1:] = data.iloc[:, 1:]/1000
	data = data.rename(columns={"外陸資買賣超股數(不含外資自營商)":"外陸資買賣超股數"})
	



if workday(date1) != False:
	show_data(json_data)
	for id in range(data.shape[0]):
		if data.iloc[id, 0] == sid:
			three.append(data.iloc[id, 5])
			items = 1
			break
d1 = datetime(int(date1[0:4]), int(date1[4:6]), int(date1[6:]))
d2 = d1 + timedelta(days = -1)
date_before = d2.strftime("%Y%m%d")
while items != 3:
	if workday(date_before) != False:
		print(date_before)
		show_data(json_data)
		for id in range(data.shape[0]):
			if data.iloc[id, 0] == sid:
				three.append(data.iloc[id, 5])
				items += 1
				d2 = d2 + timedelta(days = -1)
				date_before = d2.strftime("%Y%m%d")
	else:
		d2 = d2 + timedelta(days = -1)
		date_before = d2.strftime("%Y%m%d")

overbought = 0  # 計算連續三個工作天中買超天數
for i in three:
	if i > 0:
		overbought += 1
	else:
		overbought = 0
if overbought == 3:
	print("yes")
else:
	print("no")
		
