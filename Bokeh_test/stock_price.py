import pandas
from bokeh.plotting import figure, output_file, show

APPLE = pandas.read_csv("C:\\Users\\User\Documents\GitHub\G32-project\Bokeh_test\\AAPL.csv", parse_dates=["Date"])
p = figure(width=600, height=200, x_axis_type="datetime", title="AAPL一年股價走勢圖")
p.line(APPLE["Date"], APPLE["Close"], color="black", alpha=0.5)
show(p)
output_file("APPLE.html")