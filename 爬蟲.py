#需要先安裝lxml,requests,twstock 三個套件
# pip install stock
import twstock
twstock.__update_codes()
oneormore = input("若要查詢單股請按y,多股按任意鍵:")
one = oneormore
#輸入要一次搜尋一檔還是多檔

if one == "y":
    stockenter = input("請輸入股票代號:")
    # 輸入要搜尋的股票代號
    daysstr = input("請輸入要查詢天數:")
    # 輸入查詢天數
    days = int(daysstr)
    stock = twstock.Stock(stockenter)
    mean5 = stock.moving_average(stock.price, 5)
    mean20 = stock.moving_average(stock.price, 20)
    print("近",days."日股價:" , stock.price[-days:] , "近",days,"日的五日均線" ,  mean5[-days:], "近" , days , "日的二十日均線" , mean20[-days:])
    # 印出股價
else:
    stockenter = input("請輸入股票代號,代號間用逗號隔開:")
    stocklist = stockenter.split(",")
    # 若是查詢多股，則在輸入完後先轉成清單的形式
    stockdata = twstock.realtime.get(stocklist)
    # 然後搜尋清單內股票的即時資料
    #print(stockdata)
    #print(stockdata[stocklist[0]]["realtime"].keys())
    for i in range(len(stocklist)):    
        
        print(stockdata[stocklist[i]]["info"]["name"]+"("+stocklist[i]+")"+":"+" 收盤價:"+stockdata[stocklist[i]]["realtime"]["latest_trade_price"]
        +" 開盤價:"+stockdata[stocklist[i]]["realtime"]["open"]+" 最高價:"+stockdata[stocklist[i]]["realtime"]["high"]
        +" 最低價:"+stockdata[stocklist[i]]["realtime"]["low"])
        print(stockdata[stocklist[i]])


