import requests
import pandas as pd


def crwal_financial_report(year, season, sid):
	FinanceReportURL = "https://mops.twse.com.tw/mops/web/t163sb01"

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
	html_df = pd.read_html(r.text)[16]
	return html_df

report = crwal_financial_report(108, 3, 2330).fillna("")
# report.to_excel("Financial Report.xlsx", header=False, sheet_name=str(stock_number), index=False, startrow = 0, encoding="utf_8_sig")
print(report)
