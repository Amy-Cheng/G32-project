#需要先安裝lxml,requests,twstock 三個套件
# pip install stock
import twstock
import time
twstock.__update_codes()

stockenter = input("請輸入股票代號,代號間用逗號隔開:")
stocklist = stockenter.split(",")
# 若是查詢多股，則在輸入完後先轉成清單的形式
stockdata = twstock.realtime.get(stocklist)
# 然後搜尋清單內股票的即時資料
#print(stockdata)
#print(stockdata[stocklist[0]]["realtime"].keys())
daysstr = input("請輸入要查詢天數:")
# 輸入查詢天數
days = int(daysstr)
for i in range(len(stocklist)):    
    
    print(stockdata[stocklist[i]]["info"]["name"]+"("+stocklist[i]+")"+":"+" 收盤價:"+stockdata[stocklist[i]]["realtime"]["latest_trade_price"]
    +" 開盤價:"+stockdata[stocklist[i]]["realtime"]["open"]+" 最高價:"+stockdata[stocklist[i]]["realtime"]["high"]
    +" 最低價:"+stockdata[stocklist[i]]["realtime"]["low"]+" 時間:"+stockdata[stocklist[i]]["info"]["time"])
    #print(stockdata[stocklist[i]])

    stock = twstock.Stock(stocklist[i])
    mean5 = stock.moving_average(stock.price, 5)
    mean20 = stock.moving_average(stock.price, 20)
    capacity = stock.capacity
    for j in range(len(capacity)):
        capacity[j] = int(capacity[j]/1000)
    print("近" , days,"日股價:" , stock.price[-days:])
    print("近" , days,"日的五日均線" ,  mean5[-days:])
    print("近" , days,"日的二十日均線" , mean20[-days:])
    print("近" , days,"日的成交量(張)", capacity[-days:])
    print("倒數第二天之五日均價:",mean5[-2],"倒數第二天之二十日均價:",mean20[-2],"最後一天之五日均價:",mean5[-1],"最後一天之二十日均價:",mean20[-1])
    if mean5[-2] < mean20[-2]:
        if mean5[-1]>mean20[-1]:
            buylist.append(slist[i])
            print("五日均線突破二十日均線")
        else:
            print("五日均線仍然低於二十日均線")
            
    else:
        if mean5[-1] > mean20[-1]:
            print("五日均線仍大於二十日均線")
        else:
            print("五日均線跌破二十日均線")
    time.sleep(10)



