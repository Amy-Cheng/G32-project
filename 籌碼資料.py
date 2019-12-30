# coding=utf-8
import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime, timedelta
import scrapy
from bokeh.plotting import figure, output_file, show
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool


date1 = input()
sid = input("股票代碼：")
items = 0
y_axis = []

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
            y_axis.append(data.iloc[id, 1])
            y_axis.append(data.iloc[id, 2])
            y_axis.append(data.iloc[id, 3])
            y_axis.append(data.iloc[id, 4])
            items = 1
            break

foreign_investors = []
foreign_dealers = []
investment_trust = []
local_dealers= []
d1 = datetime(int(date1[0:4]), int(date1[4:6]), int(date1[6:]))
d2 = d1 + timedelta(days = -1)
date_before = d2.strftime("%Y%m%d")
x_axis = [d1.strftime("%Y%m%d")]
while items != 7:
    if workday(date_before) != False:
        print(date_before)
        show_data(json_data)
        for id in range(data.shape[0]):
            if data.iloc[id, 0] == sid:
                y_axis.append(data.iloc[id, 1])
                y_axis.append(data.iloc[id, 2])
                y_axis.append(data.iloc[id, 3])
                y_axis.append(data.iloc[id, 4])
                print(y_axis)
                items += 1
                x_axis.append(date_before)
                d2 = d2 + timedelta(days = -1)
                date_before = d2.strftime("%Y%m%d")
    else:
        d2 = d2 + timedelta(days = -1)
        date_before = d2.strftime("%Y%m%d")

x_axis.reverse()
y_axis.reverse()
for i in range(0,25,4):
    foreign_investors.append(y_axis[i+3])
    foreign_dealers.append(y_axis[i+2])
    investment_trust.append(y_axis[i+1])
    local_dealers.append(y_axis[i])
p = figure(title="各方買賣超股數")

p.line(x_axis, foreign_investors, legend="外陸資買賣超股數", line_color="red")
p.line(x_axis, foreign_dealers, legend="外資自營商買賣超股數", line_color="blue")
p.line(x_axis, investment_trust, legend="投信買賣超股數", line_color="green")
p.line(x_axis, local_dealers, legend="自營商買賣超股數", line_color="#9B870C")

p.legend.location = "top_left"
p.xaxis.axis_label = '日期'
p.yaxis.axis_label = '股數'

show(p)