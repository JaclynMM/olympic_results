from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap


from querydata import *

#names the graph html file
output_file ("./graphing_results.html")

#graphic colors specified
palette = ["#41ebf4", "#f4d041"]


# this creates [ ("Aquatics", "Men", "Women"), ("Archery", "Men", "Women"), ("Athletics", "Men", "Women"), ... ]
x = [ (discipline, gender) for discipline in disciplines for gender in genders ]
counts = sum(zip(data['men'], data['women']), ()) # like an hstack

#graph specs
p = figure(width=5000, height=700, toolbar_location="below", toolbar_sticky=False, x_range=FactorRange(*x),
           title="Olympic Winners by Sport & Gender")


source = ColumnDataSource(data=dict(x=x, counts=counts))

#graph bar specs
p.vbar(x='x', top='counts', width=0.5, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=genders, start=1, end=2))


p.y_range.start = 0
p.x_range.range_padding = 0.05
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)