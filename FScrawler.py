import requests
from bs4 import BeautifulSoup


sid = 2330

url = "https://histock.tw/stock/financial.aspx?no=" + str(sid) + "&st=2"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

# 擷取EPS表格
attr = {"class": "tb-stock text-center tbBasic"}
eps_info = soup.find_all("table", attrs=attr)
eps_tags = eps_info[0].find_all("td")

eps2017_2019 = []

# 2017第四季至2019第三季各季EPS
eps2017_2019.append(float(eps_tags[33].get_text()))
for eps in eps_tags[7:35:9]:
	eps2017_2019.append(float(eps.get_text()))
for eps in eps_tags[8:35:9]:
	eps2017_2019.append(float(eps.get_text()))

# 計算各季EPS年增率是否超過10%
count = 0
for i in range(4):
	eps_growth = (eps2017_2019[i + 4] / eps2017_2019[i]) - 1
	# print(eps_growth)
	if eps_growth > 0.1:
		count += 1

if count >= 3:
	print("Yes")
else:
	print("No")