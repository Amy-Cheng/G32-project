import requests
import pandas as pd
import json
import time
from datetime import datetime
import scrapy
#url = "https://www.twse.com.tw/fund/T86?response=json&date={y}{m:02d}{d:02d}&selectType=ALLBUT0999&_=1577233837182"
#https://www.twse.com.tw/fund/T86?response=json&date=20191224&selectType=ALLBUT0999&_=1577233837182
date1 = input()
dtnb = {'response': 'json', 'date': date1, 'selectType': 'ALLBUT0999', '_' : '1577233837182'}

json_data=requests.get("https://www.twse.com.tw/fund/T86", dtnb).json()

columns= ["證券代號","證券名稱","外陸資買進股數(不含外資自營商)","外陸資賣出股數(不含外資自營商)",
"外陸資買賣超股數(不含外資自營商)","外資自營商買進股數","外資自營商賣出股數","外資自營商買賣超股數",
"投信買進股數","投信賣出股數","投信買賣超股數","自營商買賣超股數","自營商買進股數(自行買賣)",
"自營商賣出股數(自行買賣)","自營商買賣超股數(自行買賣)","自營商買進股數(避險)",
"自營商賣出股數(避險)","自營商買賣超股數(避險)","三大法人買賣超股數"]

data=pd.DataFrame(json_data['data'],columns=columns)
data = data[["證券代號","外陸資買賣超股數(不含外資自營商)","外資自營商買賣超股數",
"投信買賣超股數","自營商買賣超股數","三大法人買賣超股數"]]
data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: x.replace(",", ""))
data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: int(x))
data.iloc[:, 1:] = data.iloc[:, 1:]/1000
data = data.rename(columns={"外陸資買賣超股數(不含外資自營商)":"外陸資買賣超股數"})

print(data)