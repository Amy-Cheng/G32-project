import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
import scrapy
import pandas_datareader as pdr
import mpl_finance as mpf
import datetime as datetime
import talib


slist = [2330, 2317, 2454, 3008, 1301, 2412, 2891, 1303, 1216, 2882,
		 2886, 1326, 2881, 3711, 2884, 2308, 2002, 2892, 1101, 2207,
		 2885, 5880, 2303, 3045, 5876, 2912, 2382, 2880, 5871, 2357,
		 2890, 2887, 4938, 2801, 2883, 3034, 6505, 4904, 2888, 2395,
		 2301, 1102, 2408, 1402, 9904, 2409, 2345, 3231, 2105, 2324,
		 1476, 4958, 2633, 6239, 3481, 2823, 2834, 2049, 9910, 9921,
		 2354, 2492, 2377, 2344, 3702, 2356, 2353, 1590, 2385, 2347,
		 8464, 2371, 2542, 2618, 2603, 1227, 1434, 2915, 9945, 3105,
		 5347, 8299]

name_list = {"2330": "台積電", "2317": "鴻海", "2454": "聯發科", "3008": "大立光", "1301": "台塑", 
			 "2412": "中華電", "2891": "中信金", "1303": "南亞", "1216": "統一", "2886": "兆豐金", 
			 "2882": "國泰金", "1326": "台化", "2881": "富邦金", "3711": "日月光投控", "2884": "玉山金", 
			 "2308": "台達電", "2002": "中鋼", "2892": "第一金", "1101": "台泥", "2207": "和泰車", 
			 "2885": "元大金", "5880": "合庫金", "3045": "台灣大", "2303": "聯電", "2912": "統一超", 
			 "5876": "上海商銀", "2880": "華南金", "2382": "廣達", "2357": "華碩", "5871": "中租-KY", 
			 "2474": "可成", "2890": "永豐金", "2887": "台新金", "4938": "和碩", "2801": "彰銀", 
			 "2883": "開發金", "3034": "聯詠", "6505": "台塑化", "4904": "遠傳", "2379": "瑞昱", 
			 "2888": "新光金", "2395": "研華", "2301": "光寶科", "1102": "亞泥", "2408": "南亞科", 
			 "1402": "遠東新", "2327": "國巨", "3105": "穩懋", "9904": "寶成", "2409": "友達", 
			 "3231": "緯創", "2345": "智邦", "2105": "正新", "6488": "環球晶", "2324": "仁寶", 
			 "1476": "儒鴻", "4958": "臻鼎-KY", "2633": "台灣高鐵", "6239": "力成", "3481": "群創", 
			 "5347": "世界", "2823": "中壽", "2834": "臺企銀", "2049": "上銀", "9910": "豐泰", 
			 "9921": "巨大", "2354": "鴻準", "2492": "華新科", "2377": "微星", "2344": "華邦電", 
			 "3702": "大聯大", "2356": "英業達", "2353": "宏碁", "1590": "亞德客-KY", "2385": "群光", 
			 "2347": "聯強", "6669": " 緯穎", "8299": "群聯", "8464": "億豐", "2371": "大同", 
			 "2542": "興富發", "2618": "長榮航", "2603": "長榮", "1227": "佳格", "1434": "福懋",
			 "2915": "潤泰全", "9945": "潤泰新", "2610": "華航"}




# Panel1
def stock_sma(sid):
    start = datetime.datetime(2017,1,1)

    # 取得股票資料
    if sid in [str(slist[i]) for i in range(79, 82)]:
        df = pdr.DataReader(sid + '.TWO', 'yahoo', start=start)
    else:
        df = pdr.DataReader(sid + '.TW', 'yahoo', start=start)

    df.index = df.index.format(formatter=lambda x: x.strftime('%Y-%m-%d')) 

    sma_20 = talib.SMA(np.array(df['Close']), 20)
    sma_60 = talib.SMA(np.array(df['Close']), 60)
    sma_120 = talib.SMA(np.array(df['Close']), 120)
    sma_240 = talib.SMA(np.array(df['Close']), 240)
    
    return sma_20, sma_60, sma_120, sma_240, df


# Panel2
def crwal_financial_report(sid, year, season):
	# 財報網站
	FinanceReportURL = "https://mops.twse.com.tw/mops/web/t163sb01"

	# request資訊
	form_data = {
		'encodeURIComponent':1,
        'step':1,
        'firstin':1,
        'off':1,
        'co_id':sid,
        'year': year,
        'season': season,
	}

	r = requests.post(FinanceReportURL, form_data)
	
	# 表格16為簡明合併資產負債表，19為簡明合併綜合損益表
	html_df = pd.read_html(r.text)[16].fillna("")
	return html_df

	# report = crwal_financial_report(108, 3, 2330).fillna("")
	# report.to_excel("Financial Report.xlsx", header=False, sheet_name=str(stock_number), index=False, startrow = 0, encoding="utf_8_sig")


# Panel3
def chip_data(date1, sid):
    # items作爲天數的計數器
    items = 0

    # y_axis作爲存放股數的list
    y_axis = []

    def workday(date):  # 判斷是否為工作日
        dtnb = {'response': 'json', 'date': date, 'selectType': 'ALLBUT0999', '_' : '1577233837182'}
        json_data = requests.get("https://www.twse.com.tw/fund/T86", dtnb).json()
        if json_data == {'stat': '很抱歉，沒有符合條件的資料!'} or json_data == {}:
            return False
        else:
            return json_data


    def show_data(json_data):
        columns = ["證券代號","證券名稱","外陸資買進股數(不含外資自營商)","外陸資賣出股數(不含外資自營商)",
        "外陸資買賣超股數(不含外資自營商)","外資自營商買進股數","外資自營商賣出股數","外資自營商買賣超股數",
        "投信買進股數","投信賣出股數","投信買賣超股數","自營商買賣超股數","自營商買進股數(自行買賣)",
        "自營商賣出股數(自行買賣)","自營商買賣超股數(自行買賣)","自營商買進股數(避險)",
        "自營商賣出股數(避險)","自營商買賣超股數(避險)","三大法人買賣超股數"]

        data = pd.DataFrame(json_data['data'], columns=columns)
        data = data[["證券代號","外陸資買賣超股數(不含外資自營商)","外資自營商買賣超股數",
        "投信買賣超股數","自營商買賣超股數"]]
        data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: x.replace(",", ""))
        data.iloc[:, 1:] = data.iloc[:, 1:].applymap(lambda x: int(x))
        data.iloc[:, 1:] = data.iloc[:, 1:] / 1000
        data = data.rename(columns={"外陸資買賣超股數(不含外資自營商)":"外陸資買賣超股數"})
        
        return data


    json_data = workday(date1)
    if json_data != False:
        data = show_data(json_data)
        for id in range(data.shape[0]):
            if data.iloc[id, 0] == sid:
                # 存放第一天的四個資料
                y_axis.append(data.iloc[id, 1])
                y_axis.append(data.iloc[id, 2])
                y_axis.append(data.iloc[id, 3])
                y_axis.append(data.iloc[id, 4])
                items = 1
                break
    
    # 新增4個list作爲4種資料各自存放的list
    foreign_investors = []
    foreign_dealers = []
    investment_trust = []
    local_dealers= []

    d1 = datetime.datetime(int(date1[0:4]), int(date1[4:6]), int(date1[6:]))
    d2 = d1 + datetime.timedelta(days = -1)
    date_before = d2.strftime("%Y%m%d")
    x_axis = [d1.strftime("%Y%m%d")]
    # 重複執行直到7天的數據已經存放好
    while items != 7:
        json_data = workday(date_before)
        if json_data != False:
            # print(date_before)
            data = show_data(json_data)
            for id in range(data.shape[0]):
                if data.iloc[id, 0] == sid:
                    # 根據對應天數，存放四個資料
                    y_axis.append(data.iloc[id, 1])
                    y_axis.append(data.iloc[id, 2])
                    y_axis.append(data.iloc[id, 3])
                    y_axis.append(data.iloc[id, 4])
                    items += 1
                    x_axis.append(date_before)
                    d2 = d2 + datetime.timedelta(days = -1)
                    date_before = d2.strftime("%Y%m%d")
        else:
            d2 = d2 + datetime.timedelta(days = -1)
            date_before = d2.strftime("%Y%m%d")

    # 將第一天掉換成最後一天，因x軸需要符合時間綫概念
    x_axis.reverse()
    y_axis.reverse()

    for i in range(0,25,4):
        # 因數據已經掉換，所以用反序來擷取資料
        foreign_investors.append(y_axis[i+3])
        foreign_dealers.append(y_axis[i+2])
        investment_trust.append(y_axis[i+1])
        local_dealers.append(y_axis[i])

    return x_axis, foreign_investors, foreign_dealers, investment_trust, local_dealers


# Panel4
def ratios(sid, cat_rat):
	# 匯入csv
	df102 = pd.read_excel("ratio_data\\102ratios.xlsx", index_col = 0, encoding = "utf-8")
	df103 = pd.read_excel("ratio_data\\103ratios.xlsx", index_col = 0, encoding = "utf-8")
	df104 = pd.read_excel("ratio_data\\104ratios.xlsx", index_col = 0, encoding = "utf-8")
	df105 = pd.read_excel("ratio_data\\105ratios.xlsx", index_col = 0, encoding = "utf-8")
	df106 = pd.read_excel("ratio_data\\106ratios.xlsx", index_col = 0, encoding = "utf-8")
	df107 = pd.read_excel("ratio_data\\107ratios.xlsx", index_col = 0, encoding = "utf-8")

	# 彙整各年度比率
	Ratios = []
	Years = []

	y = 101
	for i in [df102, df103, df104, df105, df106, df107]:
	    y += 1
	    try:
	        Ratios.append(i.loc[sid, cat_rat])
	        Years.append(y)
	    except:
	        pass

	Ratios = [float(x) for x in Ratios]
	dict_ratio = {"Years":Years, "Ratios":Ratios}
	df_ratios = pd.DataFrame(dict_ratio)

	return df_ratios

    
