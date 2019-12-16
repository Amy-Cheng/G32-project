from bokeh.plotting import figure, output_file, show
output_file("out.html")
p = figure()
p.line([1,2,3,4,5],[5,4,3,2,1])
show(p)
