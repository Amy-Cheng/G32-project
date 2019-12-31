import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# input
sid = int(input("輸入股票代碼>>"))
cat = input("輸入欲查詢類別>>")
rat = input("輸入欲查詢比率>>")

# 匯入csv(記得改路徑)
df101 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\101ratios.csv", index_col = 0, encoding = "utf-8")
df102 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\102ratios.csv", index_col = 0, encoding = "utf-8")
df103 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\103ratios.csv", index_col = 0, encoding = "utf-8")
df104 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\104ratios.csv", index_col = 0, encoding = "utf-8")
df105 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\105ratios.csv", index_col = 0, encoding = "utf-8")
df106 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\106ratios.csv", index_col = 0, encoding = "utf-8")
df107 = pd.read_csv("D:\\AlbertChang\\Documents\\python\\finalreport\\107ratios.csv", index_col = 0, encoding = "utf-8")

# 彙整各年度比率
Ratios = []
Years = []
y = 100
for i in [df101, df102, df103, df104, df105, df106, df107]:
    y += 1
    try:
        Ratios.append(i.loc[sid, cat + "-" + rat])
        Years.append(y)
    except:
        pass

Ratios = [float(x) for x in Ratios]
dict_ratio = {"Years":Years, "Ratios":Ratios}
df_ratios = pd.DataFrame(dict_ratio)

print(df_ratios)

# 繪圖
sns.set_style("ticks")
sns.relplot(x = "Years", y = "Ratios", data = df_ratios, kind = "line")
plt.title(sid)
plt.show()
